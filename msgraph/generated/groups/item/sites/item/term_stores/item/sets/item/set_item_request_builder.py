from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.o_data_errors import o_data_error
    from .........models.term_store import set
    from .children import children_request_builder
    from .children.item import term_item_request_builder
    from .parent_group import parent_group_request_builder
    from .relations import relations_request_builder
    from .relations.item import relation_item_request_builder
    from .terms import terms_request_builder
    from .terms.item import term_item_request_builder

class SetItemRequestBuilder():
    """
    Provides operations to manage the sets property of the microsoft.graph.termStore.store entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SetItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/termStores/{store%2Did}/sets/{set%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def children_by_id(self,id: str) -> term_item_request_builder.TermItemRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.termStore.set entity.
        Args:
            id: Unique identifier of the item
        Returns: term_item_request_builder.TermItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .children.item import term_item_request_builder
        from .terms.item import term_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["term%2Did"] = id
        return term_item_request_builder.TermItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[SetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property sets for groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SetItemRequestBuilderGetRequestConfiguration] = None) -> Optional[set.Set]:
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[set.Set]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.term_store import set

        return await self.request_adapter.send_async(request_info, set.Set, error_mapping)
    
    async def patch(self,body: Optional[set.Set] = None, request_configuration: Optional[SetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[set.Set]:
        """
        Update the navigation property sets in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[set.Set]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.term_store import set

        return await self.request_adapter.send_async(request_info, set.Set, error_mapping)
    
    def relations_by_id(self,id: str) -> relation_item_request_builder.RelationItemRequestBuilder:
        """
        Provides operations to manage the relations property of the microsoft.graph.termStore.set entity.
        Args:
            id: Unique identifier of the item
        Returns: relation_item_request_builder.RelationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .relations.item import relation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["relation%2Did"] = id
        return relation_item_request_builder.RelationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def terms_by_id(self,id: str) -> term_item_request_builder.TermItemRequestBuilder:
        """
        Provides operations to manage the terms property of the microsoft.graph.termStore.set entity.
        Args:
            id: Unique identifier of the item
        Returns: term_item_request_builder.TermItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .children.item import term_item_request_builder
        from .terms.item import term_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["term%2Did"] = id
        return term_item_request_builder.TermItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[SetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sets for groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[SetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[set.Set] = None, request_configuration: Optional[SetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sets in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.termStore.set entity.
        """
        from .children import children_request_builder

        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_group(self) -> parent_group_request_builder.ParentGroupRequestBuilder:
        """
        Provides operations to manage the parentGroup property of the microsoft.graph.termStore.set entity.
        """
        from .parent_group import parent_group_request_builder

        return parent_group_request_builder.ParentGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relations(self) -> relations_request_builder.RelationsRequestBuilder:
        """
        Provides operations to manage the relations property of the microsoft.graph.termStore.set entity.
        """
        from .relations import relations_request_builder

        return relations_request_builder.RelationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms(self) -> terms_request_builder.TermsRequestBuilder:
        """
        Provides operations to manage the terms property of the microsoft.graph.termStore.set entity.
        """
        from .terms import terms_request_builder

        return terms_request_builder.TermsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SetItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SetItemRequestBuilderGetQueryParameters():
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SetItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SetItemRequestBuilder.SetItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SetItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

