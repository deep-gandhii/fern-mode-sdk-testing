from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .agent_transfer_op_replace import AgentTransferOpReplace
from .agent_transfer_op_push import AgentTransferOpPush
from .agent_transfer_op_pop import AgentTransferOpPop


# fernMode variant type for a shared-component member of AgentTransferOp
class AgentTransferOp_Replace(AgentTransferOpReplace):
    pass


# fernMode variant type for a shared-component member of AgentTransferOp
class AgentTransferOp_Push(AgentTransferOpPush):
    pass


# fernMode variant type for a shared-component member of AgentTransferOp
class AgentTransferOp_Pop(AgentTransferOpPop):
    pass


# Union type for AgentTransferOp
# Pydantic will attempt to validate against each type in order
AgentTransferOp = Union[AgentTransferOpReplace, AgentTransferOpPush, AgentTransferOpPop]
# TypeAdapter for runtime validation of AgentTransferOp
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentTransferOp_adapter = TypeAdapter(AgentTransferOp)
