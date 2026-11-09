from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .read_metadata_chapter_db_model import ReadMetadataChapterDbModel
from .read_legal_terms import ReadLegalTerms
from .contributor import Contributor
from .preview_audio_db_model import PreviewAudioDbModel
from .sample_config_db_model import SampleConfigDbModel
from .review_response_model import ReviewResponseModel

DirectPublishingReadResponseModelDisplayMode = typing.Union[
    typing.Literal["text", "audio-only", "text-with-audio"], typing.Any
]

DirectPublishingReadResponseModelGenreItem = typing.Union[
    typing.Literal[
        "Fantasy",
        "Romance",
        "Science Fiction",
        "Mystery and Thriller",
        "Action and Adventure",
        "Dystopia",
        "Business and Economics",
        "Technology",
        "Christian & Inspirational",
        "Horror",
        "Biography and Memoir",
        "Education and Learning",
        "History",
        "Children's Literature",
        "Young Adult",
        "Fairy Tales and Folklore",
        "Fan Fiction",
        "General Fiction",
        "Health and Wellness",
        "Historical Fiction",
        "Humor",
        "Literary Classics",
        "Philosophy",
        "Poetry",
        "Politics and Government",
        "Psychology",
        "Science and Nature",
        "Self-Help",
        "Spirituality and Religion",
        "Travel",
        "True Crime",
        "Other",
    ],
    typing.Any,
]

DirectPublishingReadResponseModelTargetAudience = typing.Union[
    typing.Literal["children", "young adult", "adult", "all ages"], typing.Any
]

DirectPublishingReadResponseModelPayoutType = typing.Union[
    typing.Literal["none", "engagement_based", "fixed_payout"], typing.Any
]

DirectPublishingReadResponseModelCurrency = typing.Union[
    typing.Literal["usd"], typing.Any
]


class DirectPublishingReadResponseModel(BaseModel):
    """DirectPublishingReadResponseModel

    :param read_id: read_id
    :type read_id: str
    :param created_at_unix: created_at_unix
    :type created_at_unix: int
    :param updated_at_unix: updated_at_unix
    :type updated_at_unix: int
    :param word_count: word_count
    :type word_count: int
    :param char_count: char_count
    :type char_count: int
    :param chapters: chapters
    :type chapters: List[ReadMetadataChapterDbModel]
    :param title: title, defaults to None
    :type title: str, optional
    :param author: author, defaults to None
    :type author: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param article_image_url: article_image_url, defaults to None
    :type article_image_url: str, optional
    :param language: language, defaults to None
    :type language: str, optional
    :param locale: locale, defaults to None
    :type locale: str, optional
    :param display_mode: display_mode, defaults to None
    :type display_mode: DirectPublishingReadResponseModelDisplayMode, optional
    :param genre: genre, defaults to None
    :type genre: List[DirectPublishingReadResponseModelGenreItem], optional
    :param fiction: fiction, defaults to None
    :type fiction: str, optional
    :param content_type: content_type, defaults to None
    :type content_type: str, optional
    :param original_file_type: original_file_type, defaults to None
    :type original_file_type: str, optional
    :param target_audience: target_audience, defaults to None
    :type target_audience: DirectPublishingReadResponseModelTargetAudience, optional
    :param mature_content: mature_content, defaults to None
    :type mature_content: bool, optional
    :param safesearch_adult: safesearch_adult, defaults to None
    :type safesearch_adult: bool, optional
    :param origin: origin, defaults to None
    :type origin: str, optional
    :param publication_date: publication_date, defaults to None
    :type publication_date: str, optional
    :param isbn: isbn, defaults to None
    :type isbn: str, optional
    :param ean: ean, defaults to None
    :type ean: str, optional
    :param legal_terms: legal_terms, defaults to None
    :type legal_terms: ReadLegalTerms, optional
    :param content_guidelines_terms: content_guidelines_terms, defaults to None
    :type content_guidelines_terms: ReadLegalTerms, optional
    :param last_updated_from_project_unix: last_updated_from_project_unix, defaults to None
    :type last_updated_from_project_unix: int, optional
    :param publishing_project_id: publishing_project_id, defaults to None
    :type publishing_project_id: str, optional
    :param publishing_state: publishing_state, defaults to None
    :type publishing_state: str, optional
    :param publisher_profile_id: publisher_profile_id, defaults to None
    :type publisher_profile_id: str, optional
    :param quality_score: quality_score, defaults to None
    :type quality_score: int, optional
    :param publisher: publisher, defaults to None
    :type publisher: str, optional
    :param copyright: copyright, defaults to None
    :type copyright: str, optional
    :param subtitle: subtitle, defaults to None
    :type subtitle: str, optional
    :param distribution_territories: distribution_territories, defaults to None
    :type distribution_territories: List[str], optional
    :param edition: edition, defaults to None
    :type edition: str, optional
    :param contributors: contributors, defaults to None
    :type contributors: List[Contributor], optional
    :param payout_type: payout_type, defaults to None
    :type payout_type: DirectPublishingReadResponseModelPayoutType, optional
    :param list_price: list_price, defaults to None
    :type list_price: float, optional
    :param currency: currency, defaults to None
    :type currency: DirectPublishingReadResponseModelCurrency, optional
    :param original_audio_project_export_id: original_audio_project_export_id, defaults to None
    :type original_audio_project_export_id: str, optional
    :param original_audio_document_id: original_audio_document_id, defaults to None
    :type original_audio_document_id: str, optional
    :param series_id: series_id, defaults to None
    :type series_id: str, optional
    :param volume: volume, defaults to None
    :type volume: int, optional
    :param published_at_unix: published_at_unix, defaults to None
    :type published_at_unix: int, optional
    :param read_slug: read_slug, defaults to None
    :type read_slug: str, optional
    :param preview_audio_object: preview_audio_object, defaults to None
    :type preview_audio_object: PreviewAudioDbModel, optional
    :param sample_config: sample_config, defaults to None
    :type sample_config: SampleConfigDbModel, optional
    :param review: review, defaults to None
    :type review: ReviewResponseModel, optional
    :param voice_id: voice_id, defaults to None
    :type voice_id: str, optional
    :param can_use_assistant: can_use_assistant, defaults to None
    :type can_use_assistant: bool, optional
    :param is_voice_changer_on: is_voice_changer_on, defaults to None
    :type is_voice_changer_on: bool, optional
    """

    read_id: str
    created_at_unix: int
    updated_at_unix: int
    word_count: int
    char_count: int
    chapters: List[ReadMetadataChapterDbModel]
    title: Optional[str] = Field(default=None)
    author: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    article_image_url: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    locale: Optional[str] = Field(default=None)
    display_mode: Optional[DirectPublishingReadResponseModelDisplayMode] = Field(
        default=None
    )
    genre: Optional[List[DirectPublishingReadResponseModelGenreItem]] = Field(
        default=None
    )
    fiction: Optional[str] = Field(default=None)
    content_type: Optional[str] = Field(default=None)
    original_file_type: Optional[str] = Field(default=None)
    target_audience: Optional[DirectPublishingReadResponseModelTargetAudience] = Field(
        default=None
    )
    mature_content: Optional[bool] = Field(default=None)
    safesearch_adult: Optional[bool] = Field(default=None)
    origin: Optional[str] = Field(default=None)
    publication_date: Optional[str] = Field(default=None)
    isbn: Optional[str] = Field(default=None)
    ean: Optional[str] = Field(default=None)
    legal_terms: Optional[ReadLegalTerms] = Field(default=None)
    content_guidelines_terms: Optional[ReadLegalTerms] = Field(default=None)
    last_updated_from_project_unix: Optional[int] = Field(default=None)
    publishing_project_id: Optional[str] = Field(default=None)
    publishing_state: Optional[str] = Field(default=None)
    publisher_profile_id: Optional[str] = Field(default=None)
    quality_score: Optional[int] = Field(default=None)
    publisher: Optional[str] = Field(default=None)
    copyright: Optional[str] = Field(default=None)
    subtitle: Optional[str] = Field(default=None)
    distribution_territories: Optional[List[str]] = Field(default=None)
    edition: Optional[str] = Field(default=None)
    contributors: Optional[List[Contributor]] = Field(default=None)
    payout_type: Optional[DirectPublishingReadResponseModelPayoutType] = Field(
        default=None
    )
    list_price: Optional[float] = Field(default=None)
    currency: Optional[DirectPublishingReadResponseModelCurrency] = Field(default=None)
    original_audio_project_export_id: Optional[str] = Field(default=None)
    original_audio_document_id: Optional[str] = Field(default=None)
    series_id: Optional[str] = Field(default=None)
    volume: Optional[int] = Field(default=None)
    published_at_unix: Optional[int] = Field(default=None)
    read_slug: Optional[str] = Field(default=None)
    preview_audio_object: Optional[PreviewAudioDbModel] = Field(default=None)
    sample_config: Optional[SampleConfigDbModel] = Field(default=None)
    review: Optional[ReviewResponseModel] = Field(default=None)
    voice_id: Optional[str] = Field(default=None)
    can_use_assistant: Optional[bool] = Field(default=None)
    is_voice_changer_on: Optional[bool] = Field(default=None)
