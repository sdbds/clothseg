import launch

if not launch.is_installed("rem_bg"):
    launch.run_pip("install rem_bg", "requirements for clothseg")
