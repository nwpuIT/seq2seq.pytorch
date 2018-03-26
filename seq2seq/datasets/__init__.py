from .text import LinedTextDataset
from .open_subtitles import OpenSubtitles2016
from .wmt import WMT16_de_en
from .iwslt import IWSLT15
from .multi_language import MultiLanguageDataset
from .coco_caption import CocoCaptions

__all__ = ('LinedTextDataset',
           'OpenSubtitles2016',
           'MultiLanguageDataset',
           'WMT16_de_en',
           'IWSLT15',
           'CocoCaptions')
