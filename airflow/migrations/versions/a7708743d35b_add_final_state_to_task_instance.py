#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add final_state to task instance

Revision ID: a7708743d35b
Revises: 7939bcff74ba
Create Date: 2020-03-22 21:10:32.578282

"""

# revision identifiers, used by Alembic.
import sqlalchemy as sa
from alembic import op
revision = 'a7708743d35b'
down_revision = '7939bcff74ba'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('task_instance', sa.Column('final_state', sa.String(20)))


def downgrade():
    op.drop_column('task_instance', 'final_state')
