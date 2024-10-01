print(f"DEBUG IN_DOCKER 2: {IN_DOCKER}") # type: ignore # noqa : F821

if IN_DOCKER: # type: ignore # noqa : F821
    print("Running in Docker mode....")
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa : F821
        'django.middleware.security.SecurityMiddleware',
    ]