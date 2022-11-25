"""Base decorations."""

# ----------------------------------------------------------------------------- GENERIC
CONTEXT_BRACKET = "{grey}[{context}{grey}]"
CONTEXT_DIVIDER = "{grey}|"

PAD = "\n    {name}    \n"


# ----------------------------------------------------------------------------- BASES
ETHEREAL_ONLY   = "{grey}e"
ETHEREAL_BETTER = "{grey}+e"
ETHEREAL_GOATED = "{grey}++e"

SKILLS_ANY = "{white}+skill"
SKILLS_1   = "{white}+1"
SKILLS_2   = "{white}+2"
SKILLS_3   = "{white}+3"


# ----------------------------------------------------------------------------- RARITIES
MAGIC      = "{blue}m"
RARE       = "{yellow}r"
SET        = "{lime}s"
SET_GG     = "{lime}s+"
SET_LVL    = "{lime}lvl"
UNIQUE     = "{gold}u"
UNIQUE_LVL = "{gold}lvl"
UNIQUE_GG  = "{gold}u+"


# ----------------------------------------------------------------------------- GEMS
FLAWLESS = "~ o    Flawless    o ~"
PERFECT  = PAD.format(name="~ o  PERFECT  o ~")


# ----------------------------------------------------------------------------- RUNES
# TODO: Logic should compose keyname, derive name, and add 'real' colours.
# TODO: Logic should pad mid/high rune names to 3-char length (Um, Lo, etc.)
HR = "\n~         {name}         ~\n{purple}~        ~ ! g g ! ~       ~\n"
MR = "~    {name}    ~\n{purple}~   ~ ! -- ! ~   ~"
