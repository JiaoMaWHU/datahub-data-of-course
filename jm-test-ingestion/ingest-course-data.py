import datahub.emitter.mce_builder as builder
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.metadata.schema_classes import ChangeTypeClass, DatasetPropertiesClass
from datahub.metadata.com.linkedin.pegasus2avro.dataset import (
    DatasetLineageTypeClass,
    UpstreamClass,
    UpstreamLineage,
)
from datahub.emitter.rest_emitter import DatahubRestEmitter
from typing import List, Union

# Create an emitter to DataHub over REST
emitter = DatahubRestEmitter(
    gms_server="http://localhost:8080", extra_headers={})

# Test the connection
emitter.test_connection()


# ============================================================
# 1. Add courses
# ============================================================

# Construct a MetadataChangeProposalWrapper object.
math101_urn = builder.make_dataset_urn("course", "Math101")
math101_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=math101_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="Math101 in DataHub University",
        customProperties={
            "name": "Math 101",
            "department": "Math",
            "units": "4",
            "topics": "algebra, calculus",
            "maxCapacity": "200",
            "maxWaitlistCapacity": "400"
        }
    )
)

math102_urn = builder.make_dataset_urn("course", "Math102")
math102_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=math102_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="Math102 in DataHub University",
        customProperties={
            "name": "Math 102",
            "department": "Math",
            "units": "3",
            "topics": "disecret math, graph theory",
            "maxCapacity": "100",
            "maxWaitlistCapacity": "200"
        }
    )
)

cs101_urn = builder.make_dataset_urn("course", "CS101")
cs101_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=cs101_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="CS101 in DataHub University",
        customProperties={
            "name": "CS 101",
            "department": "Computer Science",
            "units": "4",
            "topics": "code, computer hardware, network",
            "maxCapacity": "300",
            "maxWaitlistCapacity": "500"
        }
    )
)

cs201_urn = builder.make_dataset_urn("course", "CS201")
cs201_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=cs201_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="CS201 in DataHub University",
        customProperties={
            "name": "CS 201",
            "department": "Computer Science",
            "units": "3",
            "topics": "algorithm, compute theory",
            "maxCapacity": "200",
            "maxWaitlistCapacity": "300"
        }
    )
)

# Emit metadata! This is a blocking call
emitter.emit(math101_event)
emitter.emit(math102_event)
emitter.emit(cs101_event)
emitter.emit(cs201_event)

# ============================================================
# 2. Add professors
# ============================================================

jd_urn = builder.make_dataset_urn("professor", "johndoe")
jd_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=jd_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="Professor in DataHub University",
        customProperties={
            "name": "John Doe",
            "department": "Math",
            "YOE": "4",
            "specializations": "linear algebra, complex analysis",
            "rating": "4.2/5",
            "difficulty": "3.3/5",
            "retake rate": "87%"
        }
    )
)

oy_urn = builder.make_dataset_urn("professor", "oliveyew")
oy_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=oy_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="Professor in DataHub University",
        customProperties={
            "name": "Olive Yew",
            "department": "Math",
            "YOE": "10",
            "specializations": "disecret math, graph theory",
            "rating": "2.0/5",
            "difficulty": "4.3/5",
            "retake rate": "40%"
        }
    )
)

rs_urn = builder.make_dataset_urn("professor", "raysin")
rs_event = MetadataChangeProposalWrapper(
    entityType="dataset",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=rs_urn,
    aspectName="datasetProperties",
    aspect=DatasetPropertiesClass(
        description="Professor in DataHub University",
        customProperties={
            "name": "Ray Sin",
            "department": "Computer Science",
            "YOE": "8",
            "specializations": "algorithm, compute theory",
            "rating": "4.0/5",
            "difficulty": "3.3/5",
            "retake rate": "20%"
        }
    )
)

emitter.emit(jd_event)
emitter.emit(oy_event)
emitter.emit(rs_event)

# ============================================================
# 3. Add lineage
# ============================================================

def add_lineage(upstreamUrn, downstreamUrn, type):
    upstream_tables: List[UpstreamClass] = []
    upstream_tables.append(UpstreamClass(
        dataset=upstreamUrn,
        type=type
        # type=DatasetLineageTypeClass.VIEW,
    ))

    upstream_lineage = UpstreamLineage(upstreams=upstream_tables)

    emitter = DatahubRestEmitter(
        gms_server="http://localhost:8080", extra_headers={})

    emitter.emit_mcp(MetadataChangeProposalWrapper(
        entityType="dataset",
        changeType=ChangeTypeClass.UPSERT,
        entityUrn=downstreamUrn,
        aspectName="upstreamLineage",
        aspect=upstream_lineage,
    ))

add_lineage(math101_urn, math102_urn, DatasetLineageTypeClass.TRANSFORMED)
add_lineage(math101_urn, cs101_urn, DatasetLineageTypeClass.TRANSFORMED)
add_lineage(cs101_urn, cs201_urn, DatasetLineageTypeClass.TRANSFORMED)

add_lineage(jd_urn, math101_urn, DatasetLineageTypeClass.TRANSFORMED)
add_lineage(oy_urn, math102_urn, DatasetLineageTypeClass.TRANSFORMED)
add_lineage(rs_urn, cs201_urn, DatasetLineageTypeClass.TRANSFORMED)
add_lineage(rs_urn, cs101_urn, DatasetLineageTypeClass.TRANSFORMED)