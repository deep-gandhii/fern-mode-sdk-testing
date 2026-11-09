from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .segmented_json_export_options import SegmentedJsonExportOptions
from .docx_export_options import DocxExportOptions
from .pdf_export_options import PdfExportOptions
from .txt_export_options import TxtExportOptions
from .html_export_options import HtmlExportOptions
from .srt_export_options import SrtExportOptions


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_SegmentedJson(SegmentedJsonExportOptions):
    pass


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_Docx(DocxExportOptions):
    pass


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_Pdf(PdfExportOptions):
    pass


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_Txt(TxtExportOptions):
    pass


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_Html(HtmlExportOptions):
    pass


# fernMode variant type for a shared-component member of ExportOptions
class ExportOptions_Srt(SrtExportOptions):
    pass


# Union type for ExportOptions
# Pydantic will attempt to validate against each type in order
ExportOptions = Union[
    SegmentedJsonExportOptions,
    DocxExportOptions,
    PdfExportOptions,
    TxtExportOptions,
    HtmlExportOptions,
    SrtExportOptions,
]
# TypeAdapter for runtime validation of ExportOptions
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ExportOptions_adapter = TypeAdapter(ExportOptions)
