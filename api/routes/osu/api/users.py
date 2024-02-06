from fastapi import HTTPException, APIRouter, Response, status, Form
from db.database import db

router = APIRouter()

@router.get("/users/")
def session_verify():
    return {
    "users": [
        {
            "avatar_url": "https://a.ppy.sh/7675392?1701497117.jpeg",
            "country": {
                "code": "FR",
                "name": "France"
            },
            "country_code": "FR",
            "cover": {
                "custom_url": "https://assets.ppy.sh/user-profile-covers/7675392/2d67441f9b68997ebd3c77bc98f883e29822e39e5125a40fab5a7720bada643a.jpeg",
                "id": None,
                "url": "https://assets.ppy.sh/user-profile-covers/7675392/2d67441f9b68997ebd3c77bc98f883e29822e39e5125a40fab5a7720bada643a.jpeg"
            },
            "default_group": "default",
            "groups": [],
            "id": 7675392,
            "is_active": True,
            "is_bot": False,
            "is_deleted": False,
            "is_online": True,
            "is_supporter": False,
            "last_visit": "2024-02-06T09:07:32+00:00",
            "pm_friends_only": False,
            "profile_colour": None,
            "statistics_rulesets": {
                "fruits": {
                    "count_100": 3,
                    "count_300": 105,
                    "count_50": 82,
                    "count_miss": 121,
                    "global_rank": None,
                    "global_rank_exp": None,
                    "grade_counts": {
                        "a": 0,
                        "s": 0,
                        "sh": 0,
                        "ss": 0,
                        "ssh": 0
                    },
                    "hit_accuracy": 0,
                    "is_ranked": False,
                    "level": {
                        "current": 2,
                        "progress": 29
                    },
                    "maximum_combo": 0,
                    "play_count": 3,
                    "play_time": 52,
                    "pp": 0,
                    "pp_exp": 0,
                    "ranked_score": 0,
                    "replays_watched_by_others": 0,
                    "total_hits": 190,
                    "total_score": 59348
                },
                "mania": {
                    "count_100": 5028,
                    "count_300": 29744,
                    "count_50": 538,
                    "count_miss": 1288,
                    "global_rank": None,
                    "global_rank_exp": 89906,
                    "grade_counts": {
                        "a": 13,
                        "s": 12,
                        "sh": 0,
                        "ss": 0,
                        "ssh": 0
                    },
                    "hit_accuracy": 93.002,
                    "is_ranked": False,
                    "level": {
                        "current": 23,
                        "progress": 96
                    },
                    "maximum_combo": 977,
                    "play_count": 325,
                    "play_time": 13680,
                    "pp": 0,
                    "pp_exp": 21.2113,
                    "ranked_score": 24955924,
                    "replays_watched_by_others": 0,
                    "total_hits": 35310,
                    "total_score": 88873652
                },
                "osu": {
                    "count_100": 705835,
                    "count_300": 7624409,
                    "count_50": 72472,
                    "count_miss": 238022,
                    "global_rank": 78361,
                    "global_rank_exp": 207748,
                    "grade_counts": {
                        "a": 476,
                        "s": 99,
                        "sh": 1182,
                        "ss": 8,
                        "ssh": 268
                    },
                    "hit_accuracy": 99.3722,
                    "is_ranked": True,
                    "level": {
                        "current": 100,
                        "progress": 36
                    },
                    "maximum_combo": 1760,
                    "play_count": 61341,
                    "play_time": 2779599,
                    "pp": 4930.43,
                    "pp_exp": 185.186,
                    "ranked_score": 14585845413,
                    "replays_watched_by_others": 445,
                    "total_hits": 8402716,
                    "total_score": 63731240711
                }
            },
            "username": "Lamune"
        }
    ]
}

@router.get("/users/{user_id}/")
def session_verify(resp: Response, user_id: int):
    resp.status_code = status.HTTP_200_OK
    return {
    "avatar_url": "https://a.ppy.sh/7675392?1701497117.jpeg",
    "country_code": "FR",
    "default_group": "default",
    "id": user_id,
    "is_active": True,
    "is_bot": False,
    "is_deleted": False,
    "is_online": True,
    "is_supporter": False,
    "last_visit": "2024-02-06T09:07:32+00:00",
    "pm_friends_only": False,
    "profile_colour": None,
    "username": "Lamune",
}