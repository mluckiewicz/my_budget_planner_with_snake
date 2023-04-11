    // Define the deleteRows function
    function deleteRows() {
        // Get the selected rows
        var selectedRows = $('#table').bootstrapTable('getSelections');
        var csrf_token = '{{ csrf_token }}';
        // Check if any rows are selected
        if (selectedRows.length > 0) {
            // Check if any selected rows are default
            var defaultRows = $.grep(selectedRows, function (row) {
                return row.is_default === "True";
            });
            if (defaultRows.length > 0) {
                // Show an error message if default rows are selected
                alert('Default categories cannot be deleted.');
            } else {
                // Ask the user to confirm the deletion
                if (confirm('Are you sure you want to delete the selected rows?')) {
                    // Get the IDs of the selected rows
                    var ids = $.map(selectedRows, function (row) {
                        return row.id;
                    });
                    // Send the AJAX request to delete the rows
                    $.ajax({
                        url: 'delete_categories/',
                        type: 'POST',
                        data: { 'ids': ids, csrfmiddlewaretoken: csrf_token },
                        dataType: 'json',
                        success: function (data) {
                            if (data.success) {
                                // Remove the selected rows from the table
                                $('#table').bootstrapTable('remove', {
                                    field: 'id',
                                    values: ids
                                });
                                // Show a success message
                                alert('Selected rows have been deleted.');
                            } else {
                                // Show an error message
                                alert('Failed to delete selected rows.');
                            }
                        },
                        error: function () {
                            // Show an error message
                            alert('Failed to delete selected rows.');
                        }
                    });
                }
            }
        } else {
            // Show a warning message if no rows are selected
            alert('Please select one or more rows to delete.');
        }
    }