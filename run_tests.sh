#!/bin/bash

echo "Executando testes e gerando relatório HTML..."

pytest tests/ -v --html=reports/report.html --self-contained-html

echo "Relatório gerado em reports/report.html"
