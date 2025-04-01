import os
from dotenv import load_dotenv

from atproto import Client, models
from atproto.exceptions import BadRequestError

def get_new_bio(old_bio, now_playing):
    # can be whatever
    now_playing_icon = '💽 '
    # remove everything after the now playing icon. also means that the now playing thingy will have
    # to be at the bottom
    new_bio = old_bio.split(now_playing_icon, 1)[0]
    new_bio += now_playing_icon + now_playing

    print(f'New bio: {new_bio}')
    return new_bio

def update_bio(now_playing):
    # straight up jacked from https://github.com/MarshalX/atproto/blob/main/examples/advanced_usage/update_profile.py
    load_dotenv()
    client = Client()
    client.login(os.environ['BSKY_USERNAME'], os.environ['BSKY_APP_PASSWORD'])

    try:
        current_profile_record = client.app.bsky.actor.profile.get(client.me.did, 'self')
        current_profile = current_profile_record.value
        swap_record_cid = current_profile_record.cid
    except BadRequestError:
        current_profile = swap_record_cid = None

    old_description = old_display_name = None
    if current_profile:
        old_description = current_profile.description
        old_display_name = current_profile.display_name

    new_description = get_new_bio(old_description, now_playing)

    client.com.atproto.repo.put_record(
        models.ComAtprotoRepoPutRecord.Data(
            collection=models.ids.AppBskyActorProfile,
            repo=client.me.did,
            rkey='self',
            swap_record=swap_record_cid,
            record=models.AppBskyActorProfile.Record(
                avatar=current_profile.avatar,           # keep old avatar
                banner=current_profile.banner,           # keep old banner
                pinned_post=current_profile.pinned_post, # keep old pin
                description=new_description,
                display_name=old_display_name,
            ),
        )
    )

