// Function to translate content based on selected language
function translate(language) {
    // English translations
    const translationsEnglish = {
        "police_service_forms_title": "Police Service Forms",
        "new_resident_form_title": "New resident form",
        "new_resident_form_description": "Description: People who newly shifted to this area please fill up this form",
        "character_certificate_form_title": "Character certificate form",
        "character_certificate_form_description": "Description: To apply for a character certificate fill up this form",
        "gd_form_title": "GD form",
        "gd_form_description": "Description: To file a general diary fill up this form"
    };

    // Bangla translations
    const translationsBangla = {
        "police_service_forms_title": "পুলিশ সেবা ফরম",
        "new_resident_form_title": "নতুন বাসিন্দার ফরম",
        "new_resident_form_description": "বর্ণনা: যারা এই এলাকাতে নতুনভাবে স্থানান্তরিত হন তাদের দয়া করে এই ফরম পূরণ করুন",
        "character_certificate_form_title": "চরিত্র সনদ ফরম",
        "character_certificate_form_description": "বর্ণনা: চরিত্র সনদ জারি করার জন্য এই ফরম পূরণ করুন",
        "gd_form_title": "জিডি ফরম",
        "gd_form_description": "বর্ণনা: সাধারণ ডায়েরী ফাইল করতে এই ফরম পূরণ করুন"
    };

    // Get all IDs of elements to be translated
    const ids = [
        "police_service_forms_title", "new_resident_form_title", "new_resident_form_description",
        "character_certificate_form_title", "character_certificate_form_description", "gd_form_title", "gd_form_description"
    ];

    // Update text content of elements based on the selected language
    ids.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            if (language === 'english') {
                element.textContent = translationsEnglish[id];
            } else if (language === 'bangla') {
                element.textContent = translationsBangla[id];
            }
        }
    });
}

// Function to handle language selection change
document.getElementById('language').addEventListener('change', function() {
    const selectedLanguage = this.value;
    translate(selectedLanguage);
});

// Initial translation when the page loads
translate('english'); // Set default language to English
