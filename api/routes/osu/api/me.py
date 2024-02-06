from fastapi import HTTPException, APIRouter, Response, status
from db.database import db

router = APIRouter()

@router.get("/me/")
def me(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return {
    "account_history": [],
    "active_tournament_banner": None,
    "active_tournament_banners": [],
    "avatar_url": "https://cdn.discordapp.com/attachments/886715594651615312/1204486528714281061/7675392.jpg",
    "badges": [],
    "beatmap_playcounts_count": 0,
    "comments_count": 0,
    "country": {
        "code": "FR",
        "name": "France"
    },
    "country_code": "FR",
    "cover": {
        "custom_url": None,
        "id": None,
        "url": None
    },
    "cover_url": None,
    "default_group": "default",
    "discord": None,
    "favourite_beatmapset_count": 14,
    "follower_count": 199,
    "graveyard_beatmapset_count": 0,
    "groups": [],
    "guest_beatmapset_count": 0,
    "has_supported": True,
    "id": 7675392,
    "interests": None,
    "is_active": True,
    "is_bot": False,
    "is_deleted": False,
    "is_online": True,
    "is_restricted": False,
    "is_supporter": False,
    "join_date": "2016-01-01T14:49:23+00:00",
    "kudosu": {
        "available": 0,
        "total": 0
    },
    "last_visit": "2024-02-06T09:07:32+00:00",
    "location": None,
    "loved_beatmapset_count": 0,
    "mapping_follower_count": 2,
    "max_blocks": 100,
    "max_friends": 500,
    "monthly_playcounts": [],
    "nominated_beatmapset_count": 0,
    "occupation": "Student",
    "page": {
        "html": "<div class='bbcode bbcode--profile-page'><span class=\"proportional-container js-gallery\" style=\"width:2000px;\" data-width=\"2000\" data-height=\"1312\" data-index=\"0\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/b2713f003b4db8c05fb387284d1a155d609a2112/68747470733a2f2f692e6962622e636f2f505a57303452432f77656c636f6d652d7069632e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:65.6%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/b2713f003b4db8c05fb387284d1a155d609a2112/68747470733a2f2f692e6962622e636f2f505a57303452432f77656c636f6d652d7069632e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><br /><center><br /><span class=\"proportional-container js-gallery\" style=\"width:1096px;\" data-width=\"1096\" data-height=\"612\" data-index=\"1\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/3ec45aa6f1f540f20ef44f779ab2e3751d3489a1/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f313037363833333830393431343232363031312f313037363838393130383330353135303039342f696d6167652e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:55.839416058394%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/3ec45aa6f1f540f20ef44f779ab2e3751d3489a1/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f313037363833333830393431343232363031312f313037363838393130383330353135303039342f696d6167652e706e67\" alt=\"\" loading=\"lazy\" /></span></span></center><br /><div class=\"js-spoilerbox bbcode-spoilerbox\"><a class=\"js-spoilerbox__link bbcode-spoilerbox__link\" href=\"#\"><span class=\"bbcode-spoilerbox__link-icon\"></span>Former collabs</a><div class=\"bbcode-spoilerbox__body\"><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/22757943\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"2\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/a8252f1debfeb365bca83667df95080d27dd9cb6/68747470733a2f2f7075752e73682f49513638752f653833613136633633662e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/a8252f1debfeb365bca83667df95080d27dd9cb6/68747470733a2f2f7075752e73682f49513638752f653833613136633633662e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><br /><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/9648341\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"3\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/5564d427ba349ab57dc385c14c053f8457ea7d39/68747470733a2f2f7075752e73682f49513639332f643736616431613139612e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/5564d427ba349ab57dc385c14c053f8457ea7d39/68747470733a2f2f7075752e73682f49513639332f643736616431613139612e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/11409143\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"4\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/5b84a5dc2a65e27c2d025502cb5b08a52daeca92/68747470733a2f2f7075752e73682f49513639752f643563363430616461352e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/5b84a5dc2a65e27c2d025502cb5b08a52daeca92/68747470733a2f2f7075752e73682f49513639752f643563363430616461352e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/4459449\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"5\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/4d08943545fca3777ab0b9ea1417af30fd14ff86/68747470733a2f2f7075752e73682f49513661302f336138393735386333332e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/4d08943545fca3777ab0b9ea1417af30fd14ff86/68747470733a2f2f7075752e73682f49513661302f336138393735386333332e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/10592794\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"6\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/d7525c5f40ad4fba7f257840542ab95f9581f2a0/68747470733a2f2f7075752e73682f49513661652f363632393237643632342e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/d7525c5f40ad4fba7f257840542ab95f9581f2a0/68747470733a2f2f7075752e73682f49513661652f363632393237643632342e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/7675392\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"7\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/87836a90183a3d962907b41763f94d76b0dce80f/68747470733a2f2f7075752e73682f495136616b2f373130303966393234332e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/87836a90183a3d962907b41763f94d76b0dce80f/68747470733a2f2f7075752e73682f495136616b2f373130303966393234332e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/902250\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"8\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/f991a8fd0811c6a252b7ba8222b951e543c5c548/68747470733a2f2f7075752e73682f49513661722f366566623937323164352e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/f991a8fd0811c6a252b7ba8222b951e543c5c548/68747470733a2f2f7075752e73682f49513661722f366566623937323164352e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><a rel=\"nofollow\" href=\"https://osu.ppy.sh/u/2779077\"><span class=\"proportional-container js-gallery\" style=\"width:100px;\" data-width=\"100\" data-height=\"218\" data-index=\"9\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/e4df2cf274aa0284d597fef9a186ac7f43a64030/68747470733a2f2f7075752e73682f49513661492f626330633633373764302e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:218%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/e4df2cf274aa0284d597fef9a186ac7f43a64030/68747470733a2f2f7075752e73682f49513661492f626330633633373764302e6a7067\" alt=\"\" loading=\"lazy\" /></span></span></a><br /><span class=\"proportional-container js-gallery\" style=\"width:640px;\" data-width=\"640\" data-height=\"450\" data-index=\"10\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/0d5c30e4535cc49e88d43eb9f1fdae2f39f52ab2/68747470733a2f2f692e6962622e636f2f714664674a57442f636f6c6c61622d6c616d756e6174696f6e2e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:70.3125%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/0d5c30e4535cc49e88d43eb9f1fdae2f39f52ab2/68747470733a2f2f692e6962622e636f2f714664674a57442f636f6c6c61622d6c616d756e6174696f6e2e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><img src=\"https://i.ppy.sh/b28c20e507bf2644a031aaad88ff00045973a057/68747470733a2f2f692e696d6775722e636f6d2f716b376c7a57312e6a7067\" alt=\"\" loading=\"lazy\" /><br /><span class=\"proportional-container js-gallery\" style=\"width:1920px;\" data-width=\"1920\" data-height=\"1080\" data-index=\"11\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/8e8090d650e36b27316fc276a31758e67ba3a00f/68747470733a2f2f692e6962622e636f2f4d53374c734d6a2f6e67626972642e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:56.25%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/8e8090d650e36b27316fc276a31758e67ba3a00f/68747470733a2f2f692e6962622e636f2f4d53374c734d6a2f6e67626972642e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:1199px;\" data-width=\"1199\" data-height=\"1013\" data-index=\"12\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/02e562cf87a3107a79a8541e0c95b988c648adb6/68747470733a2f2f692e6962622e636f2f784c7732344c4b2f7a6861746f782d73656469612e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:84.487072560467%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/02e562cf87a3107a79a8541e0c95b988c648adb6/68747470733a2f2f692e6962622e636f2f784c7732344c4b2f7a6861746f782d73656469612e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:1076px;\" data-width=\"1076\" data-height=\"1500\" data-index=\"13\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/4bfc7e55b408a5bc8bb1d96113247875d8b511b9/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3536343230353538383233383832373534302f3636303632353235313535333737313533342f436f6c6c61622e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:139.40520446097%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/4bfc7e55b408a5bc8bb1d96113247875d8b511b9/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3536343230353538383233383832373534302f3636303632353235313535333737313533342f436f6c6c61622e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:1500px;\" data-width=\"1500\" data-height=\"1053\" data-index=\"14\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/b6d117b2c549803e0078c4b45ce647316a733e2f/68747470733a2f2f692e6962622e636f2f443972387452422f612e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:70.2%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/b6d117b2c549803e0078c4b45ce647316a733e2f/68747470733a2f2f692e6962622e636f2f443972387452422f612e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:1500px;\" data-width=\"1500\" data-height=\"1334\" data-index=\"15\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/246c94bc728606a3f774e4d23edfdc21b878126a/68747470733a2f2f692e6962622e636f2f76716d675378332f436f6c6c61622e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:88.933333333333%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/246c94bc728606a3f774e4d23edfdc21b878126a/68747470733a2f2f692e6962622e636f2f76716d675378332f436f6c6c61622e706e67\" alt=\"\" loading=\"lazy\" /></span></span></div></div><div class=\"js-spoilerbox bbcode-spoilerbox\"><a class=\"js-spoilerbox__link bbcode-spoilerbox__link\" href=\"#\"><span class=\"bbcode-spoilerbox__link-icon\"></span>stuff</a><div class=\"bbcode-spoilerbox__body\"><span class=\"proportional-container js-gallery\" style=\"width:773px;\" data-width=\"773\" data-height=\"143\" data-index=\"16\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/b76c2c1f60ef2c8c624d498d66f58f1ad01a52e4/68747470733a2f2f692e6962622e636f2f4b35306e42794d2f6f6f662e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:18.49935316947%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/b76c2c1f60ef2c8c624d498d66f58f1ad01a52e4/68747470733a2f2f692e6962622e636f2f4b35306e42794d2f6f6f662e706e67\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:997px;\" data-width=\"997\" data-height=\"837\" data-index=\"17\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/4e13dc5ac863f22216cccf1a5d9e8302a607bbb6/68747470733a2f2f692e6962622e636f2f6d585a6b6862772f43617074753272652e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:83.9518555667%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/4e13dc5ac863f22216cccf1a5d9e8302a607bbb6/68747470733a2f2f692e6962622e636f2f6d585a6b6862772f43617074753272652e6a7067\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:1092px;\" data-width=\"1092\" data-height=\"578\" data-index=\"18\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/197229c1e5db43c3ea202ab9be5101f5cf73de71/68747470733a2f2f692e6962622e636f2f773648706e30372f436170747572652e6a7067\"><span class=\"proportional-container__height\" style=\"padding-bottom:52.930402930403%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/197229c1e5db43c3ea202ab9be5101f5cf73de71/68747470733a2f2f692e6962622e636f2f773648706e30372f436170747572652e6a7067\" alt=\"\" loading=\"lazy\" /></span></span><br /><span class=\"proportional-container js-gallery\" style=\"width:283px;\" data-width=\"283\" data-height=\"71\" data-index=\"19\" data-gallery-id=\"1688834313\" data-src=\"https://i.ppy.sh/96ed98e8a311a0e80d27b00326a1ca0eccaac68b/68747470733a2f2f692e6962622e636f2f4c726357627a712f436170747572652d642d6372616e2d323032322d30322d32362d3232343132332e706e67\"><span class=\"proportional-container__height\" style=\"padding-bottom:25.088339222615%;\"><img class=\"proportional-container__content\" src=\"https://i.ppy.sh/96ed98e8a311a0e80d27b00326a1ca0eccaac68b/68747470733a2f2f692e6962622e636f2f4c726357627a712f436170747572652d642d6372616e2d323032322d30322d32362d3232343132332e706e67\" alt=\"\" loading=\"lazy\" /></span></span></div></div></div>",
        "raw": "[img]https://i.ibb.co/PZW04RC/welcome-pic.png[/img]\n\n[centre]\n[img]https://media.discordapp.net/attachments/1076833809414226011/1076889108305150094/image.png[/img][/centre]\n[box=Former collabs]\n[url=https://osu.ppy.sh/u/22757943][img]https://puu.sh/IQ68u/e83a16c63f.jpg[/img][/url]\n[url=https://osu.ppy.sh/u/9648341][img]https://puu.sh/IQ693/d76ad1a19a.jpg[/img][/url][url=https://osu.ppy.sh/u/11409143][img]https://puu.sh/IQ69u/d5c640ada5.jpg[/img][/url][url=https://osu.ppy.sh/u/4459449][img]https://puu.sh/IQ6a0/3a89758c33.jpg[/img][/url][url=https://osu.ppy.sh/u/10592794][img]https://puu.sh/IQ6ae/662927d624.jpg[/img][/url][url=https://osu.ppy.sh/u/7675392][img]https://puu.sh/IQ6ak/71009f9243.jpg[/img][/url][url=https://osu.ppy.sh/u/902250][img]https://puu.sh/IQ6ar/6efb9721d5.jpg[/img][/url][url=https://osu.ppy.sh/u/2779077][img]https://puu.sh/IQ6aI/bc0c6377d0.jpg[/img][/url]\n[img]https://i.ibb.co/qFdgJWD/collab-lamunation.png[/img]\n[img]https://i.ppy.sh/b28c20e507bf2644a031aaad88ff00045973a057/68747470733a2f2f692e696d6775722e636f6d2f716b376c7a57312e6a7067[/img]\n[img]https://i.ibb.co/MS7LsMj/ngbird.png[/img]\n[img]https://i.ibb.co/xLw24LK/zhatox-sedia.png[/img]\n[img]https://i.ppy.sh/4bfc7e55b408a5bc8bb1d96113247875d8b511b9/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3536343230353538383233383832373534302f3636303632353235313535333737313533342f436f6c6c61622e706e67[/img]\n[img]https://i.ppy.sh/b6d117b2c549803e0078c4b45ce647316a733e2f/68747470733a2f2f692e6962622e636f2f443972387452422f612e706e67[/img]\n[img]https://i.ppy.sh/246c94bc728606a3f774e4d23edfdc21b878126a/68747470733a2f2f692e6962622e636f2f76716d675378332f436f6c6c61622e706e67[/img]\n[/box]\n[box=stuff]\n\n[img]https://i.ibb.co/K50nByM/oof.png[/img]\n[img]https://i.ibb.co/mXZkhbw/Captu2re.jpg[/img]\n[img]https://i.ibb.co/w6Hpn07/Capture.jpg[/img]\n[img]https://i.ibb.co/LrcWbzq/Capture-d-cran-2022-02-26-224123.png[/img]\n[/box]"
    },
    "pending_beatmapset_count": 0,
    "playmode": "osu",
    "playstyle": [],
    "pm_friends_only": False,
    "post_count": 0,
    "previous_usernames": [],
    "profile_colour": None,
    "profile_order": [],
    "rankHistory": None,
    "rank_highest": {},
    "rank_history": {},
    "ranked_and_approved_beatmapset_count": 0,
    "ranked_beatmapset_count": 0,
    "replays_watched_counts": [],
    "scores_best_count": 0,
    "scores_first_count": 0,
    "scores_pinned_count": 0,
    "scores_recent_count": 0,
    "session_verified": False,
    "statistics": {
        "count_100": 0,
        "count_300": 0,
        "count_50": 0,
        "count_miss": 0,
        "country_rank": 0,
        "global_rank": 20,
        "global_rank_exp": 20,
        "grade_counts": {
            "a": 0,
            "s": 0,
            "sh": 0,
            "ss": 0,
            "ssh": 0
        },
        "hit_accuracy": 100.0,
        "is_ranked": True,
        "level": {
            "current": 1,
            "progress": 0
        },
        "maximum_combo": 0,
        "play_count": 0,
        "play_time": 0,
        "pp": 0,
        "pp_exp": 0,
        "rank": {
            "country": 1
        },
        "ranked_score": 0,
        "replays_watched_by_others": 0,
        "total_hits": 0,
        "total_score": 0
    },
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
    "support_level": 0,
    "title": None,
    "title_url": None,
    "twitter": None,
    "unranked_beatmapset_count": 0,
    "user_achievements": [
        {
            "achieved_at": "2021-03-27T15:08:29Z",
            "achievement_id": 68
        },
        {
            "achieved_at": "2021-01-15T21:36:10Z",
            "achievement_id": 28
        },
        {
            "achieved_at": "2020-10-28T18:53:02Z",
            "achievement_id": 88
        },
        {
            "achieved_at": "2020-10-25T21:17:22Z",
            "achievement_id": 111
        },
        {
            "achieved_at": "2020-05-30T21:17:27Z",
            "achievement_id": 222
        },
        {
            "achieved_at": "2019-11-26T18:36:31Z",
            "achievement_id": 61
        },
        {
            "achieved_at": "2019-10-18T17:14:36Z",
            "achievement_id": 50
        },
        {
            "achieved_at": "2019-08-29T18:37:43Z",
            "achievement_id": 133
        },
        {
            "achieved_at": "2019-08-29T18:37:42Z",
            "achievement_id": 132
        },
        {
            "achieved_at": "2019-06-21T16:33:45Z",
            "achievement_id": 22
        },
        {
            "achieved_at": "2019-02-18T22:02:33Z",
            "achievement_id": 153
        },
        {
            "achieved_at": "2019-02-18T21:50:56Z",
            "achievement_id": 140
        },
        {
            "achieved_at": "2018-12-02T18:54:56Z",
            "achievement_id": 21
        },
        {
            "achieved_at": "2018-11-10T13:46:26Z",
            "achievement_id": 152
        },
        {
            "achieved_at": "2018-10-14T19:05:46Z",
            "achievement_id": 67
        },
        {
            "achieved_at": "2018-10-12T17:01:01Z",
            "achievement_id": 139
        },
        {
            "achieved_at": "2018-10-12T16:56:07Z",
            "achievement_id": 147
        },
        {
            "achieved_at": "2018-10-12T16:56:07Z",
            "achievement_id": 138
        },
        {
            "achieved_at": "2018-10-10T16:49:17Z",
            "achievement_id": 148
        },
        {
            "achieved_at": "2018-10-07T08:00:32Z",
            "achievement_id": 120
        },
        {
            "achieved_at": "2018-10-06T09:53:36Z",
            "achievement_id": 40
        },
        {
            "achieved_at": "2018-09-16T11:48:25Z",
            "achievement_id": 43
        },
        {
            "achieved_at": "2018-08-19T20:06:33Z",
            "achievement_id": 137
        },
        {
            "achieved_at": "2018-08-18T13:52:36Z",
            "achievement_id": 4
        },
        {
            "achieved_at": "2018-08-18T13:52:36Z",
            "achievement_id": 3
        },
        {
            "achieved_at": "2018-08-12T10:48:12Z",
            "achievement_id": 60
        },
        {
            "achieved_at": "2018-07-22T08:05:37Z",
            "achievement_id": 20
        },
        {
            "achieved_at": "2018-06-15T15:50:42Z",
            "achievement_id": 87
        },
        {
            "achieved_at": "2018-06-15T15:50:42Z",
            "achievement_id": 54
        },
        {
            "achieved_at": "2018-06-12T19:15:40Z",
            "achievement_id": 15
        },
        {
            "achieved_at": "2018-06-12T19:13:15Z",
            "achievement_id": 66
        },
        {
            "achieved_at": "2018-06-04T18:03:01Z",
            "achievement_id": 59
        },
        {
            "achieved_at": "2018-05-16T12:22:30Z",
            "achievement_id": 39
        },
        {
            "achieved_at": "2018-05-05T12:59:54Z",
            "achievement_id": 58
        },
        {
            "achieved_at": "2018-04-13T12:33:21Z",
            "achievement_id": 65
        },
        {
            "achieved_at": "2018-03-25T18:25:06Z",
            "achievement_id": 124
        },
        {
            "achieved_at": "2018-03-14T14:45:08Z",
            "achievement_id": 1
        },
        {
            "achieved_at": "2018-03-11T17:59:51Z",
            "achievement_id": 176
        },
        {
            "achieved_at": "2018-03-08T07:47:58Z",
            "achievement_id": 175
        },
        {
            "achieved_at": "2018-03-07T20:52:29Z",
            "achievement_id": 122
        },
        {
            "achieved_at": "2018-03-07T20:41:34Z",
            "achievement_id": 123
        },
        {
            "achieved_at": "2018-03-07T16:16:43Z",
            "achievement_id": 63
        },
        {
            "achieved_at": "2018-03-02T13:15:42Z",
            "achievement_id": 121
        },
        {
            "achieved_at": "2018-03-02T13:15:42Z",
            "achievement_id": 64
        },
        {
            "achieved_at": "2018-03-02T13:08:57Z",
            "achievement_id": 177
        },
        {
            "achieved_at": "2018-03-02T13:08:57Z",
            "achievement_id": 57
        },
        {
            "achieved_at": "2018-03-01T18:41:33Z",
            "achievement_id": 126
        },
        {
            "achieved_at": "2018-02-24T19:42:21Z",
            "achievement_id": 127
        },
        {
            "achieved_at": "2018-02-22T07:57:20Z",
            "achievement_id": 56
        },
        {
            "achieved_at": "2018-02-17T18:52:19Z",
            "achievement_id": 55
        }
    ],
    "username": "Lamune",
    "website": None
}