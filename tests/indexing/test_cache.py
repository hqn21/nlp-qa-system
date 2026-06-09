from nlp_qa_system.indexing.cache import file_sha256, load_manifest, save_manifest

def test_sha256_changes_with_content(tmp_path):
    p = tmp_path / "a.bin"
    p.write_bytes(b"hello")
    h1 = file_sha256(p)
    p.write_bytes(b"hello world")
    h2 = file_sha256(p)
    assert h1 != h2
    assert len(h1) == 64

def test_manifest_roundtrip_and_missing_default(tmp_path):
    mpath = tmp_path / "manifest.json"
    assert load_manifest(mpath) == {}
    save_manifest(mpath, {"c1.pdf": "abc"})
    assert load_manifest(mpath) == {"c1.pdf": "abc"}
