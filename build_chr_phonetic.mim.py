import pathlib
import textwrap


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def header() -> str:
    return textwrap.dedent("""
    (input-method chr Cherokee)
    (description (_ "Cherokee Syllabary Phonetic Keyboard"))
    (title "Cherokee Phonetic")
    
    (map
        (syllabary
    """)


def footer() -> str:
    return textwrap.dedent("""
        )
    )

    (state
        (init (syllabary))
    """)


def main() -> None:
    out_dir = pathlib.Path("~/.m17n.d").expanduser()
    if not out_dir.exists():
        raise RuntimeError("Missing folder  ~/.m17n.d/!")

    translit2syl: dict = dict()
    translit2syl_vowels: list = ["a", "e", "i", "o", "u", "v"]

    for syl, vowel in zip(char_range("Ꭰ", "Ꭵ"), translit2syl_vowels):
        translit2syl[vowel] = syl

    translit2syl["ga"] = "Ꭶ"
    translit2syl["ka"] = "Ꭷ"

    for syl, vowel in zip(char_range("Ꭸ", "Ꭼ"), translit2syl_vowels[1:]):
        translit2syl["g" + vowel] = syl
        translit2syl["k" + vowel] = syl

    for syl, vowel in zip(char_range("Ꭽ", "Ꮂ"), translit2syl_vowels):
        translit2syl["h" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮃ", "Ꮈ"), translit2syl_vowels):
        translit2syl["l" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮉ", "Ꮍ"), translit2syl_vowels[:-1]):
        translit2syl["m" + vowel] = syl

    translit2syl["na"] = "Ꮎ"
    # translit2syl["naH"] = "Ꮐ"
    translit2syl["hna"] = "Ꮏ"

    for syl, vowel in zip(char_range("Ꮑ", "Ꮕ"), translit2syl_vowels[1:]):
        translit2syl["n" + vowel] = syl
        translit2syl["hn" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮖ", "Ꮛ"), translit2syl_vowels):
        translit2syl["gw" + vowel] = syl
        translit2syl["kw" + vowel] = syl

    translit2syl["sa"] = "Ꮜ"
    translit2syl["s"] = "Ꮝ"

    for syl, vowel in zip(char_range("Ꮞ", "Ꮢ"), translit2syl_vowels[1:]):
        translit2syl["s" + vowel] = syl

    translit2syl["da"] = "Ꮣ"
    translit2syl["de"] = "Ꮥ"
    translit2syl["di"] = "Ꮧ"
    translit2syl["do"] = "Ꮩ"
    translit2syl["du"] = "Ꮪ"
    translit2syl["dv"] = "Ꮫ"

    translit2syl["ta"] = "Ꮤ"
    translit2syl["te"] = "Ꮦ"
    translit2syl["ti"] = "Ꮨ"
    translit2syl["to"] = "Ꮩ"
    translit2syl["tu"] = "Ꮪ"
    translit2syl["tv"] = "Ꮫ"

    translit2syl["dla"] = "Ꮬ"
    translit2syl["tla"] = "Ꮭ"

    for syl, vowel in zip(char_range("Ꮮ", "Ꮲ"), translit2syl_vowels[1:]):
        translit2syl["dl" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮳ", "Ꮸ"), translit2syl_vowels):
        translit2syl["j" + vowel] = syl
        translit2syl["z" + vowel] = syl
        translit2syl["ch" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮹ", "Ꮾ"), translit2syl_vowels):
        translit2syl["w" + vowel] = syl
        translit2syl["hw" + vowel] = syl

    for syl, vowel in zip(char_range("Ꮿ", "Ᏼ"), translit2syl_vowels):
        translit2syl["y" + vowel] = syl
        translit2syl["hy" + vowel] = syl

    # translit2syl["h"] = ""  # hopefully intrusive 'h' only

    # specials
    key: str
    for key in [*translit2syl.keys()]:
        if key.startswith("s"):
            translit2syl["ak" + key] = "ᎠᎩ" + translit2syl[key]

    # Create upper-case versions and title-case versions
    for key in [*translit2syl.keys()]:
        translit2syl[key.upper()] = translit2syl[key]
        if len(key) > 1:
            translit2syl[key[0].upper() + key[1:].lower()] = translit2syl[key]

    # Add pronunciation marks to all previous generated entries that end in a vowel [aeiouv]
    for key in [*translit2syl.keys()]:
        # IPA Lengthened
        long_vowel: str = "\u02d0"

        # Combining X Below (silent vowel)
        silent_vowel: str = "\u0353"

        # Combining Double Vertical Line Below
        high_rising_tone: str = "\u0348"

        # Combining Grave Accent Below
        low_falling_tone: str = "\u0316"

        # Combining Acute Accent Below
        high_tone: str = "\u0317"

        # Combining Caron Below
        falling_tone: str = "\u032c"

        # Combining Circumflex Accent Below
        rising_tone: str = "\u032d"

        # Combining Macron Below
        level_tone: str = "\u0331"

        if key[-1] in "aeiouvAEIOUV":
            translit2syl[key + "x"] = translit2syl[key] + silent_vowel
            translit2syl[key + "X"] = translit2syl[key] + silent_vowel

            translit2syl[key + "="] = translit2syl[key] + high_rising_tone
            translit2syl[key + "`"] = translit2syl[key] + low_falling_tone
            translit2syl[key + ">"] = translit2syl[key] + falling_tone
            translit2syl[key + "<"] = translit2syl[key] + rising_tone
            translit2syl[key + "'"] = translit2syl[key] + high_tone
            translit2syl[key + "_"] = translit2syl[key] + level_tone

            translit2syl[key + "|"] = translit2syl[key] + long_vowel

            translit2syl[key + "'|"] = translit2syl[key] + high_tone + long_vowel
            translit2syl[key + "|'"] = translit2syl[key] + high_tone + long_vowel

            translit2syl[key + "_|"] = translit2syl[key] + level_tone + long_vowel
            translit2syl[key + "|_"] = translit2syl[key] + level_tone + long_vowel

    # Output the mim file
    translit_lookup: list[str] = [*translit2syl.keys()]
    translit_lookup.sort()

    mim_text: str = header()
    for key in translit_lookup:
        mim_text += "        (\"" + key + "\" \"" + translit2syl[key] + "\")\n"
    mim_text += footer()

    with open(out_dir.joinpath("chr-phonetic.mim"), "w") as w:
        w.write(mim_text)
        w.write("\n")


if __name__ == '__main__':
    main()
