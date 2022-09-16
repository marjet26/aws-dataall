"""release 3.7.8

Revision ID: 97050ec09354
Revises: 166af5c0355b
Create Date: 2021-12-08 12:54:33.828838

"""
import datetime

from alembic import op
from sqlalchemy import Boolean, Column, String, DateTime, orm
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

from dataall.db import utils, Resource

# revision identifiers, used by Alembic.
from dataall.utils.naming_convention import (
    NamingConventionService,
    NamingConventionPattern,
)

# revision identifiers, used by Alembic.
revision = '97050ec09354'
down_revision = '166af5c0355b'
branch_labels = None
depends_on = None

Base = declarative_base()


class Dataset(Resource, Base):
    __tablename__ = 'dataset'
    environmentUri = Column(String, nullable=False)
    organizationUri = Column(String, nullable=False)
    datasetUri = Column(String, primary_key=True, default=utils.uuid('dataset'))
    region = Column(String, default='eu-west-1')
    AwsAccountId = Column(String, nullable=False)
    S3BucketName = Column(String, nullable=False)
    GlueDatabaseName = Column(String, nullable=False)
    GlueCrawlerName = Column(String)
    GlueCrawlerSchedule = Column(String)
    GlueProfilingJobName = Column(String)
    GlueProfilingTriggerSchedule = Column(String)
    GlueProfilingTriggerName = Column(String)
    GlueDataQualityJobName = Column(String)
    GlueDataQualitySchedule = Column(String)
    GlueDataQualityTriggerName = Column(String)
    IAMDatasetAdminRoleArn = Column(String, nullable=False)
    IAMDatasetAdminUserArn = Column(String, nullable=False)
    KmsAlias = Column(String, nullable=False)
    language = Column(String, nullable=False, default='English')
    topics = Column(postgresql.ARRAY(String), nullable=True)
    confidentiality = Column(String, nullable=False, default='Unclassified')
    tags = Column(postgresql.ARRAY(String))
    bucketCreated = Column(Boolean, default=False)
    glueDatabaseCreated = Column(Boolean, default=False)
    iamAdminRoleCreated = Column(Boolean, default=False)
    iamAdminUserCreated = Column(Boolean, default=False)
    kmsAliasCreated = Column(Boolean, default=False)
    lakeformationLocationCreated = Column(Boolean, default=False)
    bucketPolicyCreated = Column(Boolean, default=False)
    businessOwnerEmail = Column(String, nullable=True)
    businessOwnerDelegationEmails = Column(postgresql.ARRAY(String), nullable=True)
    stewards = Column(String, nullable=True)
    SamlAdminGroupName = Column(String, nullable=True)
    importedS3Bucket = Column(Boolean, default=False)
    importedGlueDatabase = Column(Boolean, default=False)
    importedKmsKey = Column(Boolean, default=False)
    importedAdminRole = Column(Boolean, default=False)
    imported = Column(Boolean, default=False)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    print('Back filling datasets crawler names...')
    datasets: [Dataset] = session.query(Dataset).all()
    dataset: Dataset
    for dataset in datasets:
        print(f'Back fill dataset crawler name {dataset.label}...')
        dataset.GlueCrawlerName = f'{dataset.S3BucketName}-crawler'
    session.commit()
    print('Successfully back filled glue crawler names ')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
