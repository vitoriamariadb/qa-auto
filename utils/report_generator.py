import json
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_html(self, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"report_{timestamp}.html"

        html_content = self._build_html(results)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return filename

    def _build_html(self, results):
        total = results.get('total', 0)
        passed = results.get('passed', 0)
        failed = results.get('failed', 0)

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Relatório de Testes</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .summary {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
        .passed {{ color: green; }}
        .failed {{ color: red; }}
    </style>
</head>
<body>
    <h1>Relatório de Testes - qa-auto</h1>
    <div class="summary">
        <p><strong>Total de Testes:</strong> {total}</p>
        <p class="passed"><strong>Passou:</strong> {passed}</p>
        <p class="failed"><strong>Falhou:</strong> {failed}</p>
        <p><strong>Data:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>
        """
        return html

    def generate_json(self, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"report_{timestamp}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)

        return filename
