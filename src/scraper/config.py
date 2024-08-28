from pathlib import Path

# relative to this config file
CACHE_DIR = Path(__file__).parent.parent.parent / "cache"

SITES = {
    "UC_Berkeley": {
        "name": "UC Berkeley",
        "type": "squares",
        "subjectCodesUrl": "https://guide.berkeley.edu/courses/",
        "selectors": {
            "code": ".courseblocktitle .code",
            "title": ".courseblocktitle .title",
            "description": lambda el: el.select_one(".descshow br").nextSibling,
        },
    },
    "UC_Davis": {
        "name": "UC Davis",
        "type": "squares",
        "subjectCodesUrl": "https://catalog.ucdavis.edu/courses-subject-code/",
        "selectors": {
            "code": ".detail-code b",
            "title": lambda el: el.select_one(".detail-title b").text.lstrip("— "),
            "description": lambda el: el.select_one(".courseblockextra em").nextSibling,
        },
    },
    "UC_Irvine": {
        "name": "UC Irvine",
        "type": "squares",
        "subjectCodesUrl": "https://catalogue.uci.edu/allcourses/",
        "selectors": {
            "code": lambda el: el.select_one(".courseblocktitle strong").text.split(
                ".  "
            )[0],
            "title": lambda el: el.select_one(".courseblocktitle strong").text.split(
                ".  "
            )[1],
            "description": ".courseblockdesc p:first-child",
        },
    },
    "CSU_East_Bay": {
        "name": "CSU East Bay",
        "type": "modern_campus",
        "urlBase": "https://catalog.csueastbay.edu",
        "startUrl": "https://catalog.csueastbay.edu/content.php?catoid=35&navoid=30996",
        "selectors": {
            "code": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                0
            ],
            "title": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                1
            ],
            "description": lambda el: el.select_one(
                "#course_preview_title ~ br"
            ).nextSibling,
        },
    },
    "Fresno_State": {
        "name": "Fresno State",
        "type": "modern_campus",
        "urlBase": "https://catalog.fresnostate.edu",
        "startUrl": "https://catalog.fresnostate.edu/content.php?catoid=5&navoid=193",
        "selectors": {
            "code": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                0
            ],
            "title": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                1
            ],
            "description": lambda el: el.select_one(
                "#course_preview_title + hr"
            ).nextSibling,
        },
    },
}
