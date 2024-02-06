from fastapi import HTTPException, APIRouter, Response, status
from db.database import db

router = APIRouter()

@router.get("/friends")
def friends(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return [
        {
        "avatar_url": "https://osu.ppy.sh/images/layout/avatar-guest.png",
        "country": {
            "code": "FR",
            "name": "France"
        },
        "country_code": "FR",
        "cover": {
            "custom_url": None,
            "id": "6",
            "url": "https://osu.ppy.sh/images/headers/profile-covers/c6.jpg"
        },
        "default_group": "default",
        "groups": [],
        "id": 16105749,
        "is_active": False,
        "is_bot": False,
        "is_deleted": False,
        "is_online": False,
        "is_supporter": False,
        "last_visit": "2020-02-10T17:38:33+00:00",
        "pm_friends_only": False,
        "profile_colour": None,
        "statistics": {
            "count_100": 170,
            "count_300": 486,
            "count_50": 45,
            "count_miss": 52,
            "global_rank": None,
            "global_rank_exp": None,
            "grade_counts": {
                "a": 0,
                "s": 0,
                "sh": 0,
                "ss": 0,
                "ssh": 0
            },
            "hit_accuracy": 76.6009,
            "is_ranked": False,
            "level": {
                "current": 5,
                "progress": 8
            },
            "maximum_combo": 184,
            "play_count": 8,
            "play_time": 646,
            "pp": 0,
            "pp_exp": 0,
            "ranked_score": 573396,
            "replays_watched_by_others": 0,
            "total_hits": 701,
            "total_score": 748596
        },
        "support_level": 0,
        "username": "_Xanthos_"
    }
    ]