if ak_is_group_member(request.user, name="wazuh-administrators"):
    yield "wazuh-admin"