
-- post hook can be moved into dbt_project.yml so that it applies to all models

{{ config(
    materialized='incremental',
    incremental_strategy='append',
    post_hook=[
        "DELETE FROM {{this}} WHERE event_datetime < date_sub(TIMESTAMP '{{var('start_date')}}', 2)",
        "CALL {{var('catalog')}}.system.expire_snapshots(table => '{{this}}', older_than => TIMESTAMP '2022-12-12', retain_last => 4)",
        "CALL {{var('catalog')}}.system.remove_orphan_files(table => '{{this}}', dry_run => false)",
    ]
) }}

select
    TIMESTAMP '{{var('start_date')}}' as event_datetime,
    named_struct('f1', 1, 'f2', 'allo', 'farray', array(1,2,3)) as complex, 
    * 
from 
    {{ ref('stg_orders') }}
