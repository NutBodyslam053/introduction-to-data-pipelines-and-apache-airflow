import great_expectations as ge

def _validate_data():
    columns = ["NewConfirmed", "Date"]
    my_df = ge.read_csv("data.csv", names=columns)
    print(my_df)

    results = my_df.expect_column_values_to_be_between(
        column="NewConfirmed",
        min_value=0,
        max_value=322315,
    )
    print(results)

    assert results["success"] is True


_validate_data()
