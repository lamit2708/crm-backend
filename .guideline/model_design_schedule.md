# Design the model for the customer appointment

[Ref](https://docs.google.com/spreadsheets/d/1RvSU4x9W5z2Zf9AO4KSYJ2ce8dTAU33asQ_gfTiXNNg/edit#gid=1570745569)

## Schedule with bitwise

[Microsoft Schedule](https://docs.microsoft.com/en-us/sql/relational-databases/system-tables/dbo-sysschedules-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15)

[REF](https://stackoverflow.com/questions/12089431/database-table-design-for-scheduling-tasks)

Schedule

- ScheduleName
- ScheduleTypeId (Daily, Weekly, Monthly, Yearly, Specific)
- StartDate
- IntervalInDays
- Frequency
- FrequencyCounter

ScheduleDaily

- ScheduleDailyId
- ScheduleId
- TimeOfDay
- StartDate
- EndDate

ScheduleMonthly

- ScheduleMonthlyId
- ScheduleId
- DayOfMonth
- StartDate
- EndDate

ScheduleSpecific

- ScheduleSpecificId
- ScheduleId
- SpecificDate
- StartDate

ScheduleJob

- ScheduleJobId
- ScheduleId
- ScheduleTypeId
- RunDate
- ScheduleStatusId

## Reference Laravel Rule

[REF](https://laravel.com/docs/8.x/scheduling)
