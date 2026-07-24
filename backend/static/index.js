let currentTab = 'skills';
let resumeText = '';
let currentCoverLetter = '';

// Tab switching
function switchTab(tab) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.add('hidden');
    });

    // Remove active class from all buttons
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(`${tab}-tab`).classList.remove('hidden');
    event.target.classList.add('active');

    currentTab = tab;
    hideResults();
}

// Toggle resume input method
function toggleResumeInputMethod(method) {
    if (method === 'upload') {
        document.getElementById('resume-upload-section').style.display = 'block';
        document.getElementById('resume-paste-section').style.display = 'none';
    } else {
        document.getElementById('resume-upload-section').style.display = 'none';
        document.getElementById('resume-paste-section').style.display = 'block';
    }
}

// File handling
function handleFileSelect(event, type) {
    const file = event.target.files[0];
    if (file) {
        uploadFile(file, type);
    }
}

function handleDrop(event, type) {
    event.preventDefault();
    event.target.classList.remove('dragover');
    const file = event.dataTransfer.files[0];
    if (file) {
        uploadFile(file, type);
    }
}

function handleDragOver(event) {
    event.preventDefault();
    event.target.classList.add('dragover');
}

function handleDragLeave(event) {
    event.target.classList.remove('dragover');
}

async function uploadFile(file, type) {
    const formData = new FormData();
    formData.append('file', file);

    const endpoint = type === 'resume' ? '/api/upload-resume' : '/api/upload-jd';

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            if (type === 'resume') {
                resumeText = result.text;
                document.getElementById('resume-file-info').innerHTML = 
                    `<i class="fas fa-check text-green-400 mr-2"></i> ${file.name} uploaded successfully (${result.word_count} words)`;
            }
        } else {
            showError(result.error);
        }
    } catch (error) {
        showError('File upload failed: ' + error.message);
    }
}

// Skills JD upload functions
let skillsJDText = '';

function toggleSkillsJDMethod(method) {
    const uploadDiv = document.getElementById('skills-jd-upload');
    const manualDiv = document.getElementById('skills-jd-manual');

    if (method === 'upload') {
        uploadDiv.classList.remove('hidden');
        manualDiv.classList.add('hidden');
    } else {
        uploadDiv.classList.add('hidden');
        manualDiv.classList.remove('hidden');
    }
}

async function handleSkillsJDUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/api/upload-jd', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.success) {
                skillsJDText = result.text;
                document.getElementById('skills-jd-file-info').innerHTML = 
                    `<i class="fas fa-check text-green-400 mr-2"></i> ${file.name} uploaded successfully (${result.word_count} words)`;
            } else {
                showError(result.error);
            }
        } catch (error) {
            showError('File upload failed: ' + error.message);
        }
    }
}

// Generation functions
async function generateFromSkills() {
    const userInput = document.getElementById('skills-input').value;
    const years = document.getElementById('skills-years').value;
    const experience = document.getElementById('skills-experience-auto').value;
    const targetRole = document.getElementById('skills-role').value;
    const company = document.getElementById('skills-company').value;

    // Debug logging
    console.log('🔍 Frontend Debug - Years input:', years);
    console.log('🔍 Frontend Debug - User input:', userInput);
    console.log('🔍 Frontend Debug - Experience level:', experience);

    // Get job description based on input method
    const jdMethod = document.querySelector('input[name="skills-jd-method"]:checked').value;
    let jobDescription = '';

    if (jdMethod === 'upload') {
        jobDescription = skillsJDText;
        if (!jobDescription.trim()) {
            showError('Please upload a job description file first');
            return;
        }
    } else {
        jobDescription = document.getElementById('skills-jd').value;
        if (!jobDescription.trim()) {
            showError('Please enter a job description');
            return;
        }
    }

    if (!userInput.trim()) {
        showError('Please enter your skills and experience');
        return;
    }

    // Let backend handle experience extraction naturally - no forced enhancement
    let enhancedUserInput = userInput;
    console.log('🔍 Skills Debug - Original input:', userInput);
    console.log('🔍 Skills Debug - Years provided:', years);
    console.log('🔍 Skills Debug - Experience level:', experience);
    
    // Only add basic info if completely missing, let backend do the sophisticated extraction
    if (!userInput.toLowerCase().includes('year') && !userInput.toLowerCase().includes('experience') && years && years !== '0' && years !== '') {
        enhancedUserInput = `${userInput} Experience: ${years} years`;
        console.log('🔍 Skills Debug - Minimal enhancement:', enhancedUserInput);
    } else {
        console.log('🔍 Skills Debug - Using original input, backend will handle extraction');
    }

    await generateCoverLetter('skills', enhancedUserInput, jobDescription, targetRole, company, '', experience);
}

async function generateFromResume() {
    const jobDescription = document.getElementById('resume-jd').value;
    const years = document.getElementById('resume-years').value;
    const experience = document.getElementById('resume-experience-auto').value;
    const targetRole = document.getElementById('resume-role').value;
    const company = document.getElementById('resume-company').value;

    // Debug logging
    console.log('🔍 Resume Debug - Years input:', years);
    console.log('🔍 Resume Debug - Experience level:', experience);

    // Get resume text based on input method
    const resumeMethod = document.querySelector('input[name="resume-input-method"]:checked').value;
    let resumeInput = '';

    if (resumeMethod === 'upload') {
        resumeInput = resumeText;
        if (!resumeInput.trim()) {
            showError('Please upload your resume first');
            return;
        }
    } else {
        resumeInput = document.getElementById('resume-text').value;
        if (!resumeInput.trim()) {
            showError('Please paste your resume text');
            return;
        }
    }

    if (!jobDescription.trim()) {
        showError('Please enter the job description');
        return;
    }

    console.log('🔍 Resume Debug - Resume input length:', resumeInput.length);
    console.log('🔍 Resume Debug - Before enhancement:', resumeInput.substring(0, 100) + '...');

    // Let backend handle experience extraction naturally - no forced enhancement
    let enhancedResumeInput = resumeInput;
    console.log('🔍 Resume Debug - Original input:', resumeInput.substring(0, 100) + '...');
    console.log('🔍 Resume Debug - Years provided:', years);
    console.log('🔍 Resume Debug - Experience level:', experience);
    
    // Only add basic info if completely missing, let backend do the sophisticated extraction
    if (!resumeInput.toLowerCase().includes('year') && !resumeInput.toLowerCase().includes('experience') && years && years !== '0' && years !== '') {
        enhancedResumeInput = `${resumeInput} Experience: ${years} years`;
        console.log('🔍 Resume Debug - Minimal enhancement:', enhancedResumeInput.substring(0, 150) + '...');
    } else {
        console.log('🔍 Resume Debug - Using original input, backend will handle extraction');
    }

    await generateCoverLetter('resume', enhancedResumeInput, jobDescription, targetRole, company, enhancedResumeInput, experience);
}

async function generateFromManual() {
    const userInput = document.getElementById('manual-input').value;
    const jobDescription = document.getElementById('manual-jd').value;
    const years = document.getElementById('manual-years').value;
    const experience = document.getElementById('manual-experience-auto').value;
    const targetRole = document.getElementById('manual-role').value;
    const company = document.getElementById('manual-company').value;

    // Debug logging
    console.log('🔍 Manual Debug - Years input:', years);
    console.log('🔍 Manual Debug - User input:', userInput);
    console.log('🔍 Manual Debug - Experience level:', experience);

    if (!userInput.trim()) {
        showError('Please enter your information');
        return;
    }

    if (!jobDescription.trim()) {
        showError('Please enter the job description');
        return;
    }

    // Let backend handle experience extraction naturally - no forced enhancement
    let enhancedUserInput = userInput;
    console.log('🔍 Manual Debug - Original input:', userInput);
    console.log('🔍 Manual Debug - Years provided:', years);
    console.log('🔍 Manual Debug - Experience level:', experience);
    
    // Only add basic info if completely missing, let backend do the sophisticated extraction
    if (!userInput.toLowerCase().includes('year') && !userInput.toLowerCase().includes('experience') && years && years !== '0' && years !== '') {
        enhancedUserInput = `${userInput} Experience: ${years} years`;
        console.log('🔍 Manual Debug - Minimal enhancement:', enhancedUserInput);
    } else {
        console.log('🔍 Manual Debug - Using original input, backend will handle extraction');
    }

    await generateCoverLetter('manual_jd', enhancedUserInput, jobDescription, targetRole, company, '', experience);
}

async function generateCoverLetter(method, userInput, jobDescription, targetRole, company, resumeText = '', experience = '') {
    showLoading();
    hideResults();

    // Debug logging - what's being sent to API
    console.log('🔍 API Debug - Method:', method);
    console.log('🔍 API Debug - User Input:', userInput);
    console.log('🔍 API Debug - Job Description:', jobDescription);
    console.log('🔍 API Debug - Target Role:', targetRole);
    console.log('🔍 API Debug - Company:', company);
    console.log('🔍 API Debug - Resume Text:', resumeText);
    console.log('🔍 API Debug - Experience Level:', experience);

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                method: method,
                user_input: userInput,
                job_description: jobDescription,
                target_role: targetRole,
                company: company,
                resume_text: resumeText,
                experience_level: experience
            })
        });

        const result = await response.json();

        // Debug logging - what's received from backend
        console.log('🔍 Response Debug - Full result:', result);
        console.log('🔍 Response Debug - Success:', result.success);
        console.log('🔍 Response Debug - Cover letter preview:', result.cover_letter ? result.cover_letter.substring(0, 200) + '...' : 'No cover letter');
        console.log('🔍 Response Debug - Generation info:', result.generation_info);

        if (result.success) {
            displayResults(result.cover_letter, result.generation_info);
        } else {
            showError(result.error);
        }
    } catch (error) {
        showError('Generation failed: ' + error.message);
    } finally {
        hideLoading();
    }
}

// UI functions
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('error-message').classList.add('hidden');
}

function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}

function displayResults(coverLetter, stats) {
    console.log('🔍 Display Debug - Cover letter received:', coverLetter ? coverLetter.substring(0, 200) + '...' : 'No cover letter');
    console.log('🔍 Display Debug - Stats received:', stats);

    // Clear any existing content first
    const contentElement = document.getElementById('cover-letter-content');
    contentElement.textContent = '';

    // Force DOM update
    setTimeout(() => {
        currentCoverLetter = coverLetter;
        contentElement.textContent = coverLetter;

        // Debug - check what's actually in the content element
        const displayedContent = contentElement.textContent;
        console.log('🔍 Display Debug - Actually displayed:', displayedContent ? displayedContent.substring(0, 200) + '...' : 'No content displayed');
        console.log('🔍 Display Debug - Contains "5 years":', displayedContent.includes('5 years'));
        console.log('🔍 Display Debug - Contains "0 years":', displayedContent.includes('0 years'));

        if (stats) {
            const experienceText = stats.experience_level ? ` • Experience: ${stats.experience_level}` : '';
            document.getElementById('generation-stats').innerHTML = 
                `Generated in ${stats.method} mode • ${stats.word_count} words • ${stats.character_count} characters • Target: ${stats.target_role}${experienceText}`;
        }

        document.getElementById('results').classList.remove('hidden');
        document.getElementById('error-message').classList.add('hidden');
    }, 100); // Small delay to ensure DOM update
}

function hideResults() {
    document.getElementById('results').classList.add('hidden');
    document.getElementById('error-message').classList.add('hidden');
}

function showError(message) {
    document.getElementById('error-text').textContent = message;
    document.getElementById('error-message').classList.remove('hidden');
    document.getElementById('results').classList.add('hidden');
    hideLoading();
}

function copyToClipboard() {
    const text = document.getElementById('cover-letter-content').textContent;
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('copy-btn');
        btn.classList.add('copied');
        btn.innerHTML = '<i class="fas fa-check mr-2"></i> Copied!';

        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="fas fa-copy mr-2"></i> Copy';
        }, 2000);
    });
}

function downloadCoverLetter() {
    const text = document.getElementById('cover-letter-content').textContent;
    const blob = new Blob([text], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'cover-letter.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Auto-categorize experience based on years
function categorizeExperience(years) {
    const yearsNum = parseInt(years) || 0;
    const select = document.getElementById('skills-experience-auto');

    if (yearsNum <= 1) {
        select.value = 'fresher';
    } else if (yearsNum <= 5) {
        select.value = 'mid-level';
    } else if (yearsNum <= 10) {
        select.value = 'senior';
    } else {
        select.value = 'expert';
    }
}

// Add event listener for years input
document.addEventListener('DOMContentLoaded', function() {
    // Set initial states
    toggleResumeInputMethod('upload');

    // Add years input listeners for all sections
    const skillsYearsInput = document.getElementById('skills-years');
    const resumeYearsInput = document.getElementById('resume-years');
    const manualYearsInput = document.getElementById('manual-years');

    // Skills section
    if (skillsYearsInput) {
        skillsYearsInput.addEventListener('input', function() {
            // console.log('🔍 Skills Years Input Changed:', this.value);
            categorizeExperience(this.value, 'skills-experience-auto');
        });
        categorizeExperience(skillsYearsInput.value, 'skills-experience-auto');
    }

    // Resume section
    if (resumeYearsInput) {
        resumeYearsInput.addEventListener('input', function() {
            // console.log('🔍 Resume Years Input Changed:', this.value);
            categorizeExperience(this.value, 'resume-experience-auto');
        });
        categorizeExperience(resumeYearsInput.value, 'resume-experience-auto');
    }

    // Manual section
    if (manualYearsInput) {
        manualYearsInput.addEventListener('input', function() {
            // console.log('🔍 Manual Years Input Changed:', this.value);
            categorizeExperience(this.value, 'manual-experience-auto');
        });
        categorizeExperience(manualYearsInput.value, 'manual-experience-auto');
    }
});

// Updated categorize function to accept select element ID
function categorizeExperience(years, selectId = 'skills-experience-auto') {
    const yearsNum = parseInt(years) || 0;
    const select = document.getElementById(selectId);

    // console.log(`🔍 Categorize Debug - Years: ${years}, Select ID: ${selectId}, Years Num: ${yearsNum}`);

    if (select) {
        if (yearsNum <= 1) {
            select.value = 'fresher';
        } else if (yearsNum <= 5) {
            select.value = 'mid-level';
        } else if (yearsNum <= 10) {
            select.value = 'senior';
        } else {
            select.value = 'expert';
        }
        // console.log(`🔍 Categorize Debug - Set to: ${select.value}`);
    } else {
        // console.log(`🔍 Categorize Debug - Select element not found: ${selectId}`);
    }
}