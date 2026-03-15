import pkgutil, os, site

site_packages = site.getsitepackages()[0]

def get_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except:
                pass
    return total

packages = []
for module in pkgutil.iter_modules([site_packages]):
    path = os.path.join(site_packages, module.name)
    if os.path.exists(path):
        packages.append((module.name, get_size(path)))

for name, size in sorted(packages, key=lambda x: x[1], reverse=True):
    print(f"{name:30} {size/1024/1024:.2f} MB")