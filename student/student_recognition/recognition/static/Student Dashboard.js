document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    let data = {
        branch: formData.get('branch'),
        year1_marks: formData.get('year1_marks'),
        year2_marks: formData.get('year2_marks'),
        year3_marks: formData.get('year3_marks'),
        year4_marks: formData.get('year4_marks'),
        achievements: formData.get('achievements'),
        activities: formData.get('activities'),
        certificates: []
    };

    // Get the uploaded files
    const certificates = formData.getAll('certificates[]');
    certificates.forEach((file, index) => {
        data.certificates.push({
            name: file.name,
            size: file.size,
            type: file.type
        });
    });

    // Convert the data to JSON
    const jsonData = JSON.stringify(data, null, 2);

    // Log the JSON data to the console
    console.log(jsonData);

    // Example: You can send this JSON data to a server
    // fetch('submit_form.php', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //     },
    //     body: jsonData,
    // }).then(response => response.json()).then(result => {
    //     console.log('Success:', result);
    // }).catch(error => {
    //     console.error('Error:', error);
    // });
});