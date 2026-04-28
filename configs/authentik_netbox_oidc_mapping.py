# Custom OIDC Property Mapping for NetBox SSO Integration
# Purpose: Maps the user's immutable UUID rather than a mutable username or email.
# This strictly prevents the creation of duplicate/orphaned accounts in downstream applications
# if a user's email address or display name changes in the IdP.

def map_custom_claims(request):
    return {
        # Pass the immutable UUID as the primary subject/identifier
        "sub_uuid": request.user.uuid.hex,
        
        # Pass standard claims for display purposes within the NetBox UI
        "preferred_username": request.user.username,
        "email": request.user.email,
        "name": request.user.name,
        
        # Enforce RBAC by passing assigned Authentik groups to NetBox roles
        "groups": [group.name for group in request.user.ak_groups.all()],
        
        # Security/Audit flags
        "is_active": request.user.is_active,
        "is_superuser": request.user.is_superuser
    }

return map_custom_claims(request)