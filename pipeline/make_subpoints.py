"""Build data/subpoints.json: where the Earth and the Sun are, seen from the Moon's centre.

One JPL Horizons call (target Moon 301, observer Earth centre 500@399) gives, every 6 hours,
the sub-Earth point (quantity 14), the sub-solar point (15), the Sun-Moon range r (19)
and the Earth-Moon range delta (20). All in the MOON_ME frame, east longitude, 1737.4 km
sphere (stated in the Horizons header). We keep 6-hour rows and store Moon-centred
x, y, z vectors, so the page can find the Sun and Earth direction from ANY site at ANY time:

    v = vector - 1737.4 km * site_up      (the subtraction is the parallax step; Earth is
                                           off by ~0.26 deg without it)
    azimuth = atan2(v.east, v.north), elevation = asin(v.up / |v|)

Interpolate between rows with a 4-point cubic in x, y, z (never in lon/lat).
Run: python pipeline/make_subpoints.py
"""
import datetime, json, math, os, sys, urllib.parse, urllib.request

API = "https://ssd.jpl.nasa.gov/api/horizons.api"
START, STOP = "2026-01-01 00:00", "2036-01-01 00:00"
STEP_HOURS = 6          # hours between rows (cubic interpolation at 6 h adds < 0.00001 deg)
AU_KM = 149597870.7
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "subpoints.json")


def fetch():
    params = {
        "format": "json", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "OBSERVER",
        "COMMAND": "'301'", "CENTER": "'500@399'",
        "START_TIME": f"'{START}'", "STOP_TIME": f"'{STOP}'", "STEP_SIZE": f"'{STEP_HOURS} h'",
        "QUANTITIES": "'14,15,19,20'", "ANG_FORMAT": "DEG", "EXTRA_PREC": "YES",
        "CSV_FORMAT": "YES", "CAL_FORMAT": "JD",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=600) as r:
        return json.load(r)["result"]


def parse(text):
    header = text.split("$$SOE")[0]
    # The header line reads "Target pole/equ : MOON_ME" (mean Earth frame). Anything else
    # (e.g. IAU_MOON or a PA frame) would shift a polar site by hundreds of metres.
    if "MOON_ME" not in header and "MEAN_ME" not in header:
        sys.exit("Horizons header does not name the Moon mean-Earth frame; check it.")
    rows = []
    for line in text.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines():
        c = [x.strip() for x in line.split(",")]
        # JD, flag, flag, ObsSub-LON, ObsSub-LAT, SunSub-LON, SunSub-LAT, r, rdot, delta, deldot
        rows.append((float(c[0]), float(c[3]), float(c[4]), float(c[5]), float(c[6]),
                     float(c[7]) * AU_KM, float(c[9]) * AU_KM))
    return rows


def xyz(lon_deg, lat_deg, dist_km):
    lo, la = math.radians(lon_deg), math.radians(lat_deg)
    return (dist_km * math.cos(la) * math.cos(lo), dist_km * math.cos(la) * math.sin(lo),
            dist_km * math.sin(la))


def main():
    rows = parse(fetch())
    kept = rows
    earth, sun = [], []
    for jd, elon, elat, slon, slat, r_sun, d_earth in kept:
        earth += [round(v) for v in xyz(elon, elat, d_earth)]            # km
        sun += [round(v / 1000) for v in xyz(slon, slat, r_sun)]        # thousand km
    out = {
        "source": "JPL Horizons API, target 301 (Moon), observer 500@399, quantities 14,15,19,20",
        "frame": "MOON_ME (DE421 mean Earth), east longitude, sphere R=1737.4 km",
        "generated_from": f"{START} to {STOP} UT, every {STEP_HOURS} h",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "versions": {"ephemeris": "JPL Horizons API, DE441 (Moon target, geocentric observer)"},
        "jd0": kept[0][0], "step_hours": STEP_HOURS, "n": len(kept),
        "earth_km": earth, "sun_1000km": sun,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"{len(rows)} rows at {STEP_HOURS} h, wrote {os.path.normpath(OUT)} "
          f"({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
