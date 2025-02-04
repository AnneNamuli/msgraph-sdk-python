from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

class AssignedLicense(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new assignedLicense and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A collection of the unique identifiers for plans that have been disabled.
        self._disabled_plans: Optional[List[UUID]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier for the SKU.
        self._sku_id: Optional[UUID] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignedLicense
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignedLicense()
    
    @property
    def disabled_plans(self,) -> Optional[List[UUID]]:
        """
        Gets the disabledPlans property value. A collection of the unique identifiers for plans that have been disabled.
        Returns: Optional[List[UUID]]
        """
        return self._disabled_plans
    
    @disabled_plans.setter
    def disabled_plans(self,value: Optional[List[UUID]] = None) -> None:
        """
        Sets the disabledPlans property value. A collection of the unique identifiers for plans that have been disabled.
        Args:
            value: Value to set for the disabled_plans property.
        """
        self._disabled_plans = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "disabledPlans": lambda n : setattr(self, 'disabled_plans', n.get_collection_of_primitive_values(UUID)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("disabledPlans", self.disabled_plans)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sku_id(self,) -> Optional[UUID]:
        """
        Gets the skuId property value. The unique identifier for the SKU.
        Returns: Optional[UUID]
        """
        return self._sku_id
    
    @sku_id.setter
    def sku_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the skuId property value. The unique identifier for the SKU.
        Args:
            value: Value to set for the sku_id property.
        """
        self._sku_id = value
    

