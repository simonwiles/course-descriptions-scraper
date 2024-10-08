from pathlib import Path

# relative to this config file
CACHE_DIR = Path(__file__).parent.parent.parent / "cache"

SITES = {
    "CSU_Bakersfield": {
        "name": "CSU Bakersfield",
        "type": "courseleaf",
        "subjectCodesUrl": "https://catalog.csub.edu/course-descriptions/",
        "selectors": {
            "code": ".detail-code",
            "title": ".detail-title",
            # Permit missing description (.courseblockextra) element
            "description": lambda el: getattr(
                el.select_one(".courseblockextra"), "text", ""
            ),
        },
    },
    "CSU_Chico": {
        "name": "CSU Chico",
        "type": "courseleaf",
        "subjectCodesUrl": "https://catalog.csuchico.edu/courses/",
        "selectors": {
            "code": ".detail-code",
            "title": ".detail-title",
            "description": ".detail-description",
        },
    },
    "CSU_Dominguez_Hills": {
        "name": "CSU Dominguez Hills",
        "type": "courseleaf",
        "subjectCodesUrl": "https://catalog.csudh.edu/courses/",
        "selectors": {
            "code": lambda el: el.select_one(".detail-code").text.rstrip("."),
            "title": lambda el: el.select_one(".detail-title").text.rstrip("."),
            # The last .courseblockextra element is always "Offered ...", but sometimes
            #  it's the only one; take a description only if there's more than one
            "description": lambda el: (
                courseblockextra := el.select(".courseblockextra"),
                "" if not len(courseblockextra) > 1 else courseblockextra[0].text,
            )[-1],
        },
    },
    "CSU_East_Bay": {
        "name": "CSU East Bay",
        "type": "moderncampus",
        "startUrl": "https://catalog.csueastbay.edu/content.php?catoid=35&navoid=30996",
        "selectors": {
            "code": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                0
            ],
            "title": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                1
            ],
        },
    },
    "Fresno_State": {
        "name": "Fresno State",
        "type": "moderncampus",
        "startUrl": "https://catalog.fresnostate.edu/content.php?catoid=5&navoid=193",
        "selectors": {
            "code": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                0
            ],
            "title": lambda el: el.select_one("#course_preview_title").text.split(" - ")[
                1
            ],
        },
    },
    "UC_Berkeley": {
        "name": "UC Berkeley",
        "type": "courseleaf",
        "subjectCodesUrl": "https://guide.berkeley.edu/courses/",
        "selectors": {
            "code": ".courseblocktitle .code",
            "title": ".courseblocktitle .title",
            # Text content from the .descshow element minus the part before the first
            #  <br/> element plus the text from the .deschide element if it exists
            "description": lambda el: (
                descshow := el.select_one(".descshow"),
                descshow.contents[0].extract(),
                descshow.text,
            )[-1]
            + getattr(el.select_one(".deschide"), "text", ""),
        },
    },
    "UC_Davis": {
        "name": "UC Davis",
        "type": "courseleaf",
        "subjectCodesUrl": "https://catalog.ucdavis.edu/courses-subject-code/",
        "selectors": {
            "code": ".detail-code b",
            "title": lambda el: el.select_one(".detail-title b").text.lstrip("— "),
            # Text content from the .courseblockextra element minus the part before
            #  the first <br/> element
            "description": lambda el: (
                courseblockextra := el.select_one(".courseblockextra"),
                courseblockextra.contents[0].extract(),
                courseblockextra.text,
            )[-1],
        },
    },
    "UC_Irvine": {
        "name": "UC Irvine",
        "type": "courseleaf",
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
    "UCLA": {
        "name": "UCLA",
        "type": "ucla",
    },
    "UC_San_Francisco": {
        "name": "UC San Francisco",
        "type": "courseleaf",
        "subjectCodesUrl": "https://catalog.ucsf.edu/course-catalog/",
        "selectors": {
            "code": ".detail-code",
            "title": ".detail-title",
            "description": ".courseblockextra:not(.noindent)",
        },
    },
}
