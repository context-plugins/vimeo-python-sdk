from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoCcLang1(str, Enum):
    """The language in which the automated closed captions appear.

    Option descriptions:
     * ``af`` - The language is Afrikaans.
     * ``am`` - The language is Amharic.
     * ``ar`` - The language is Arabic.
     * ``as`` - The language is Assamese.
     * ``ast`` - The language is Asturian.
     * ``az`` - The language is Azerbaijani.
     * ``be`` - The language is Belarusian.
     * ``bg`` - The language is Bulgarian.
     * ``bn`` - The language is Bengali.
     * ``bs`` - The language is Bosnian.
     * ``ca`` - The language is Catalan.
     * ``ceb`` - The language is Cebuano.
     * ``cs`` - The language is Czech.
     * ``cy`` - The language is Welsh.
     * ``da`` - The language is Danish.
     * ``de`` - The language is German.
     * ``el`` - The language is Greek.
     * ``en`` - The language is English.
     * ``es`` - The language is Spanish.
     * ``et`` - The language is Estonian.
     * ``fa`` - The language is Persian.
     * ``ff`` - The language is Fulah.
     * ``fi`` - The language is Finnish.
     * ``fil`` - The language is Filipino.
     * ``fr`` - The language is French.
     * ``ga`` - The language is Irish.
     * ``gl`` - The language is Galician.
     * ``gu`` - The language is Gujarati.
     * ``ha`` - The language is Hausa.
     * ``he`` - The language is Hebrew.
     * ``hi`` - The language is Hindi.
     * ``hr`` - The language is Croatian.
     * ``hu`` - The language is Hungarian.
     * ``hy`` - The language is Armenian.
     * ``id`` - The language is Indonesian.
     * ``ig`` - The language is Igbo.
     * ``is`` - The language is Icelandic.
     * ``it`` - The language is Italian.
     * ``ja`` - The language is Japanese.
     * ``jv`` - The language is Javanese.
     * ``ka`` - The language is Georgian.
     * ``kea`` - The language is Kabuverdianu.
     * ``kk`` - The language is Kazakh.
     * ``km`` - The language is Khmer.
     * ``kn`` - The language is Kannada.
     * ``ko`` - The language is Korean.
     * ``ku`` - The language is Kurdish.
     * ``ky`` - The language is Kyrgyz.
     * ``lb`` - The language is Luxembourgish.
     * ``lg`` - The language is Ganda.
     * ``ln`` - The language is Lingala.
     * ``lo`` - The language is Lao.
     * ``lt`` - The language is Lithuanian.
     * ``luo`` - The language is Luo.
     * ``lv`` - The language is Latvian.
     * ``mi`` - The language is Maori.
     * ``mk`` - The language is Macedonian.
     * ``ml`` - The language is Malayalam.
     * ``mn`` - The language is Mongolian.
     * ``mr`` - The language is Marathi.
     * ``ms`` - The language is Malay.
     * ``mt`` - The language is Maltese.
     * ``my`` - The language is Burmese.
     * ``ne`` - The language is Nepali.
     * ``nl`` - The language is Dutch.
     * ``no`` - The language is Norwegian.
     * ``nso`` - The language is Northern Sotho.
     * ``ny`` - The language is Nyanja.
     * ``oc`` - The language is Occitan.
     * ``or`` - The language is Odia.
     * ``pa`` - The language is Punjabi.
     * ``pl`` - The language is Polish.
     * ``ps`` - The language is Pashto.
     * ``pt`` - The language is Portuguese.
     * ``ro`` - The language is Romanian.
     * ``ru`` - The language is Russian.
     * ``sd`` - The language is Sindhi.
     * ``sk`` - The language is Slovak.
     * ``sl`` - The language is Slovenian.
     * ``sn`` - The language is Shona.
     * ``so`` - The language is Somali.
     * ``sr`` - The language is Serbian.
     * ``sv`` - The language is Swedish.
     * ``sw`` - The language is Swahili.
     * ``ta`` - The language is Tamil.
     * ``te`` - The language is Telugu.
     * ``tg`` - The language is Tajik.
     * ``th`` - The language is Thai.
     * ``tr`` - The language is Turkish.
     * ``uk`` - The language is Ukrainian.
     * ``umb`` - The language is Umbundu.
     * ``ur`` - The language is Urdu.
     * ``uz`` - The language is Uzbek.
     * ``vi`` - The language is Vietnamese.
     * ``wo`` - The language is Wolof.
     * ``xh`` - The language is Xhosa.
     * ``zh`` - The language is Chinese.
     * ``zh-HK`` - The language is Cantonese (Hong Kong).
     * ``zu`` - The language is Zulu."""

    AF = "af"
    AM = "am"
    AR = "ar"
    AS = "as"
    AST = "ast"
    AZ = "az"
    BE = "be"
    BG = "bg"
    BN = "bn"
    BS = "bs"
    CA = "ca"
    CEB = "ceb"
    CS = "cs"
    CY = "cy"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    ES = "es"
    ET = "et"
    FA = "fa"
    FF = "ff"
    FI = "fi"
    FIL = "fil"
    FR = "fr"
    GA = "ga"
    GL = "gl"
    GU = "gu"
    HA = "ha"
    HE = "he"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    HY = "hy"
    ID = "id"
    IG = "ig"
    IS = "is"
    IT = "it"
    JA = "ja"
    JV = "jv"
    KA = "ka"
    KEA = "kea"
    KK = "kk"
    KM = "km"
    KN = "kn"
    KO = "ko"
    KU = "ku"
    KY = "ky"
    LB = "lb"
    LG = "lg"
    LN = "ln"
    LO = "lo"
    LT = "lt"
    LUO = "luo"
    LV = "lv"
    MI = "mi"
    MK = "mk"
    ML = "ml"
    MN = "mn"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MY = "my"
    NE = "ne"
    NL = "nl"
    NO = "no"
    NSO = "nso"
    NY = "ny"
    OC = "oc"
    OR = "or"
    PA = "pa"
    PL = "pl"
    PS = "ps"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SD = "sd"
    SK = "sk"
    SL = "sl"
    SN = "sn"
    SO = "so"
    SR = "sr"
    SV = "sv"
    SW = "sw"
    TA = "ta"
    TE = "te"
    TG = "tg"
    TH = "th"
    TR = "tr"
    UK = "uk"
    UMB = "umb"
    UR = "ur"
    UZ = "uz"
    VI = "vi"
    WO = "wo"
    XH = "xh"
    ZH = "zh"
    ZH_HK = "zh-HK"
    ZU = "zu"

    __str__ = str.__str__


AutoCcLang1OrStr: TypeAlias = Annotated[AutoCcLang1 | str, open_enum_validator(AutoCcLang1)]
