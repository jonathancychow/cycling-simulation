import sys
import subprocess
from cycling.model.frontend.index import app


def main():
    app.run_server(host='0.0.0.0', port=8050)


def production():
    rt = subprocess.call(
        ["gunicorn", "cycling.model.frontend.index:app.server", "--bind", "0.0.0.0:8050"])
    if rt != 0:
        print(f'Gunicorn server exited with non-zero exit code {rt}')
    sys.exit(rt)


if __name__ == '__main__':
    main()
