"""Build a Search Console-like .zip from a folder of CSV fixtures (used inside tests)."""
import zipfile
from pathlib import Path


def make_zip(src_dir, dest_zip, utf8_flag=True):
    """Zip every file of src_dir (flat).

    utf8_flag=False writes UTF-8 entry names WITHOUT the UTF-8 flag, as some tools
    do; readers that trust the default cp437 then see mojibake.
    """
    src_dir, dest_zip = Path(src_dir), Path(dest_zip)
    original = zipfile.ZipInfo._encodeFilenameFlags
    if not utf8_flag:
        def raw_utf8(self):
            return self.filename.encode("utf-8"), self.flag_bits & ~0x800
        zipfile.ZipInfo._encodeFilenameFlags = raw_utf8
    try:
        with zipfile.ZipFile(dest_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(src_dir.iterdir()):
                if f.is_file():
                    z.write(f, arcname=f.name)
    finally:
        zipfile.ZipInfo._encodeFilenameFlags = original
    return dest_zip
