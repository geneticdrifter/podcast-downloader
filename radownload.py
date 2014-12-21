import gmusicapi

mm=gmusicapi.Musicmanager()

mm.__init__(debug_logging=True, validate=True, verify_ssl=True)
mm.login(oauth_credentials='/Users/Ames/Google Drive/Python/podcast_downloader/oauth.cred')
mm.upload('/Users/Ames/Google Drive/Python/podcast_downloader/798wunaesther.mp3')