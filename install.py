import launch

if not launch.is_installed("rem_bg"):
    launch.run_pip("install rembg", "requirements for clothseg")
