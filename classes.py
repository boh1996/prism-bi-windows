__author__ = 'Bo'
class Contact:
    skype_name = "",
    full_name = "",
    profile_attachment = "",
    boddy_status = "",
    given_display_name = "",
    display_name = "",
    about = ""

class Call:
    guid = "",
    duration = 0,
    type = 0,
    status = 0,
    start_timestamp = 0,
    creation_timestamp = 0,
    call_name = "",
    begin_timestamp = 0

class Conversation:
    chat_name = ""

class Chat:
    name = "",
    timestamp = 0,
    topic = "",
    activity_timestamp = 0,
    last_change = 0

class Message:
        skype_name = "",
        chat_identifier = "",
        display_name = "",
        message_type = 0,
        message = "",
        media = "",
        time_sent = 0