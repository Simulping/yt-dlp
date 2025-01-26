from .common import InfoExtractor
from ..utils import ExtractorError, classproperty, remove_start


class UnsupportedInfoExtractor(InfoExtractor):
    IE_DESC = False
    URLS = ()  # Redefine in subclasses

    @classproperty
    def IE_NAME(cls):
        return remove_start(super().IE_NAME, 'Known')

    @classproperty
    def _VALID_URL(cls):
        return rf'https?://(?:www\.)?(?:{"|".join(cls.URLS)})'


LF = '\n       '


class KnownDRMIE(UnsupportedInfoExtractor):
    """Sites that are known to use DRM for all their videos

    Add to this list only if:
    * You are reasonably certain that the site uses DRM for ALL their videos
    * Multiple users have asked about this site on github/discord
    """

    URLS = (
        r'urmomlmaooooooooooooooooooooooooo\.com',
    )

    _TESTS = []

    def _real_extract(self, url):
        raise ExtractorError(
            f'The requested site is known to use DRM protection. '
            f'It will {self._downloader._format_err("NOT", self._downloader.Styles.EMPHASIS)} be supported.{LF}'
            f'Please {self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open an issue, '
            'unless you have evidence that the video is not DRM protected', expected=True)


class KnownPiracyIE(UnsupportedInfoExtractor):
    """Sites that have been deemed to be piracy

    In order for this to not end up being a catalog of piracy sites,
    only sites that were once supported should be added to this list
    """

    URLS = (
        r'urmomlmaooooooooooooooooooooooooo\.com',
    )

    _TESTS = []

    def _real_extract(self, url):
        raise ExtractorError(
            f'This website is no longer supported since it has been determined to be primarily used for piracy.{LF}'
            f'{self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open issues for it', expected=True)
