"""
Advanced Cover Letter Generator Module
Basic implementation for web server functionality
"""

from typing import Dict, List, Optional, Tuple
import re
import random
import time
from datetime import datetime


class CoverLetterGenerator:
    """Advanced cover letter generator with dynamic personalization."""
    
    def __init__(self):
        """Initialize the Advanced Cover Letter Generator."""
        # Don't set a fixed seed to allow for true randomness and variation
        # The system time will naturally provide variation between runs
        pass
        
        self.templates = {
            'fresher': self._get_fresher_templates(),
            'experienced': self._get_experienced_templates(),
            'mid-level': self._get_mid_level_templates()
        }
        
        # Enhanced skill database with more web technologies
        self.skill_database = {
            'programming': ['python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'go', 'rust'],
            'web': ['react', 'vue', 'angular', 'nodejs', 'express', 'django', 'flask', 'spring', 'html', 'css', 'html5', 'css3'],
            'database': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle', 'database'],
            'cloud': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform'],
            'ai_ml': ['machine learning', 'tensorflow', 'pytorch', 'nlp', 'computer vision'],
            'tools': ['git', 'agile', 'scrum', 'jenkins', 'ci/cd', 'linux', 'windows']
        }
        
        # Dynamic opening phrases
        self.opening_phrases = [
            "I am writing to express my strong interest in the",
            "I am excited to apply for the",
            "I am thrilled to submit my application for the",
            "I would like to express my enthusiasm for the",
            "I am delighted to apply for the position of"
        ]
        
        # Dynamic closing phrases
        self.closing_phrases = [
            "I look forward to discussing how my skills and experience can benefit your team.",
            "I am eager to explore how my background aligns with your needs.",
            "I would welcome the opportunity to discuss my qualifications further.",
            "I appreciate your time and consideration of my application.",
            "Thank you for reviewing my application. I am excited about the possibility of contributing to your team."
        ]
    
    def _create_skill_narrative(self, skills: str, experience_level: str, years: str) -> str:
        """Create a coherent narrative from skills based on experience level."""
        skills_list = [skill.strip().lower() for skill in skills.split(',')]
        
        # Define skill categories and narratives
        if experience_level == 'fresher':
            if any(skill in skills_list for skill in ['python', 'java', 'javascript']):
                return f"strong foundation in {skills} with academic projects demonstrating practical application"
            elif any(skill in skills_list for skill in ['react', 'vue', 'angular']):
                return f"proficiency in modern frontend technologies including {skills}"
            else:
                return f"comprehensive training in {skills} with hands-on project experience"
                
        elif experience_level == 'mid-level':
            if any(skill in skills_list for skill in ['python', 'java', 'node.js']):
                return f"{years} of professional experience developing robust solutions with {skills}"
            elif any(skill in skills_list for skill in ['react', 'vue', 'css']):
                return f"{years} creating responsive user interfaces and modern web applications using {skills}"
            else:
                return f"{years} of diverse experience with {skills} across multiple projects"
                
        else:  # experienced
            if any(skill in skills_list for skill in ['python', 'java', 'go']):
                return f"extensive background in {skills} with expertise in system architecture and optimization"
            elif any(skill in skills_list for skill in ['react', 'angular', 'typescript']):
                return f"deep expertise in frontend development with {skills} and modern frameworks"
            else:
                return f"comprehensive mastery of {skills} with leadership and architectural experience"
    
    def _group_related_skills(self, skills_list: List[str]) -> List[str]:
        """Group related skills for better narrative flow."""
        # Define skill groups
        backend = ['python', 'java', 'node.js', 'go', 'spring', 'django', 'flask']
        frontend = ['react', 'vue', 'angular', 'typescript', 'javascript', 'html', 'css']
        database = ['mysql', 'postgresql', 'mongodb', 'redis']
        cloud = ['aws', 'azure', 'gcp', 'docker', 'kubernetes']
        
        # Group skills by category
        grouped = []
        for skill in skills_list:
            skill_lower = skill.lower()
            if skill_lower in backend and not any(b in grouped for b in backend if b.lower() in skill_lower):
                backend_skills = [s for s in skills_list if s.lower() in backend]
                if len(backend_skills) > 1:
                    grouped.append(f"{', '.join(backend_skills[:-1])} and {backend_skills[-1]}")
                else:
                    grouped.extend(backend_skills)
            elif skill_lower in frontend and not any(f in grouped for f in frontend if f.lower() in skill_lower):
                frontend_skills = [s for s in skills_list if s.lower() in frontend]
                if len(frontend_skills) > 1:
                    grouped.append(f"{', '.join(frontend_skills[:-1])} and {frontend_skills[-1]}")
                else:
                    grouped.extend(frontend_skills)
            elif skill_lower not in [g.lower() for g in grouped]:
                grouped.append(skill)
        
        return grouped[:6]  # Limit to 6 skills
    
    def _get_fresher_templates(self) -> List[str]:
        """Get templates for freshers/entry-level positions."""
        return [
            """Dear {hiring_manager},

{opening_phrase} {position} position at {company}. As a recent graduate with a strong foundation in {key_skills}, I am eager to bring my fresh perspective and enthusiasm to your team.

During my academic career, I developed {specialized_skills} through coursework and projects. My experience with {matched_content} has prepared me to contribute effectively to your team's objectives. I've worked on several projects that required me to apply theoretical knowledge to real-world challenges, which has strengthened my problem-solving abilities.

I am particularly drawn to {company} because of your commitment to {company_values}. This aligns perfectly with my own values of {professional_values} and my desire to work for an organization that values innovation and growth. Your company's work in {dynamic_content} especially resonates with my career aspirations.

As a fresher, I bring a unique combination of theoretical knowledge and practical skills. I am a quick learner, adaptable, and passionate about {specialized_skills}. My academic projects have honed my problem-solving abilities and taught me the importance of collaboration and attention to detail. I believe my fresh perspective could bring new ideas to your team.

I would welcome the opportunity to discuss how my education, skills, and enthusiasm can benefit {company}. Thank you for considering my application.

{closing_phrase}

{candidate_name}""",
            
            """Dear {hiring_manager},

{opening_phrase} {position} role at {company}. As a motivated recent graduate with comprehensive training in {key_skills}, I am excited to begin my professional journey with a forward-thinking organization like yours.

My academic background has provided me with a solid foundation in {specialized_skills}, complemented by hands-on experience through various projects and internships. I have developed strong analytical and problem-solving skills that I am eager to apply in a professional setting. During my internships, I had the opportunity to work on real-world projects that taught me the importance of teamwork and meeting deadlines.

What particularly attracts me to {company} is your reputation for {company_values}. I am impressed by your innovative approach to {dynamic_content} and believe my fresh perspective and eagerness to learn would make me a valuable addition to your team. I've been following {company}'s projects and am particularly inspired by your recent work.

As a recent graduate, I offer a unique combination of up-to-date theoretical knowledge and practical application skills. I am proficient in {key_skills} and have demonstrated my ability to quickly adapt to new technologies and methodologies. I'm excited about the opportunity to contribute my energy and fresh ideas to your established team.

I am excited about the possibility of contributing my skills and enthusiasm to {company}. I would appreciate the opportunity to discuss how I can add value to your team.

{closing_phrase}

{candidate_name}""",
            
            """Dear {hiring_manager},

I am writing to express my strong interest in the {position} position at {company}. As a recent graduate passionate about {key_skills}, I am eager to apply my academic knowledge and practical skills in a professional environment.

Throughout my education, I have developed a strong foundation in {specialized_skills} through rigorous coursework and hands-on projects. My experience with {matched_content} has equipped me with the technical abilities and problem-solving mindset needed to contribute effectively to your team's objectives. I have successfully completed projects that demonstrate my ability to translate theoretical concepts into practical solutions.

{company}'s commitment to {company_values} and innovation in {dynamic_content} deeply resonates with my career aspirations. I am particularly impressed by your organization's approach to emerging technologies and believe my fresh perspective would be valuable to your team.

As an entry-level professional, I bring enthusiasm, adaptability, and a strong desire to learn and grow. I am proficient in {key_skills} and have demonstrated my ability to quickly master new technologies and collaborate effectively in team environments. I am confident that my combination of academic excellence and practical skills makes me a strong candidate for this position.

I would welcome the opportunity to discuss how my background and skills can benefit {company}. Thank you for your time and consideration.

{closing_phrase}

{candidate_name}"""
        ]
    
    def _get_experienced_templates(self) -> List[str]:
        """Get templates for experienced professionals."""
        return [
            """Dear {hiring_manager},

{opening_phrase} {position} position at {company}. With {years_experience} of professional experience in {key_skills}, I am confident that my expertise aligns perfectly with your requirements.

Throughout my career, I have consistently demonstrated excellence in {specialized_skills}. My experience with {matched_content} has enabled me to deliver measurable results and drive successful outcomes for my employers. I am particularly proud of my achievements in {key_achievements}, where I successfully led cross-functional teams to deliver projects ahead of schedule.

I have been following {company}'s work for some time and am deeply impressed by your commitment to {company_values}. Your innovative approach to {dynamic_content} resonates with my own professional philosophy and career aspirations. I particularly admire how {company} has positioned itself as a leader in the industry, and I'm excited about the possibility of contributing to your continued growth.

My professional journey has equipped me with comprehensive expertise in {key_skills}. I have successfully led projects, mentored team members, and contributed to strategic initiatives that have delivered significant business value. My ability to combine technical excellence with strategic thinking makes me an ideal candidate for this role. I believe my experience in navigating complex challenges would be valuable to your team.

I would welcome the opportunity to discuss how my experience and skills can contribute to {company}'s continued success. Thank you for considering my application.

{closing_phrase}

{candidate_name}""",
            
            """Dear {hiring_manager},

{opening_phrase} {position} opportunity at {company}. As a seasoned professional with {years_experience} of experience specializing in {key_skills}, I am excited about the possibility of bringing my expertise to your esteemed organization.

My professional background includes extensive work in {specialized_skills}, where I have consistently delivered exceptional results. My experience with {matched_content} has prepared me to tackle complex challenges and drive meaningful impact. I have a proven track record of {key_achievements}.

{company}'s reputation for excellence in {company_values} is well-known in our industry, and I am particularly drawn to your innovative approach to {dynamic_content}. I believe my experience and professional philosophy align perfectly with your organizational values and objectives.

Over the course of my career, I have developed deep expertise in {key_skills}, complemented by strong leadership abilities and strategic thinking. I have successfully managed complex projects, mentored junior professionals, and contributed to organizational growth and innovation.

I am eager to discuss how my background and expertise can benefit {company}. Thank you for your time and consideration.

{closing_phrase}

{candidate_name}"""
        ]
    
    def _get_mid_level_templates(self) -> List[str]:
        """Get templates for mid-level professionals."""
        return [
            """Dear {hiring_manager},

{opening_phrase} {position} position at {company}. With {years_experience} of experience in {key_skills}, I have developed the expertise and professional maturity needed to excel in this role and contribute meaningfully to your team.

My career has been focused on building comprehensive skills in {specialized_skills}. Through various roles and projects, I have gained hands-on experience with {matched_content}, which has prepared me to handle the responsibilities outlined in your job description. I am particularly proud of my contributions to {key_achievements}, where I successfully delivered projects that exceeded expectations and drove measurable business impact.

I have long admired {company}'s {dynamic_content}. Your organization's culture of excellence and continuous learning aligns perfectly with my professional values and career aspirations. I've been particularly impressed by how {company} fosters innovation while maintaining high standards of quality.

As a mid-level professional, I bring {value_proposition}. I have experience in {key_skills} and have developed strong problem-solving abilities, project management skills, and the capacity to work effectively in cross-functional teams. I believe my experience in bridging technical solutions with business needs would be valuable to your organization.

{closing_phrase}

Thank you for your consideration.

Sincerely,
{candidate_name}""",
            
            """Dear {hiring_manager},

{opening_phrase} {position} role at {company}. As a professional with {years_experience} of experience in {key_skills}, I have developed the skills and expertise needed to make an immediate and meaningful contribution to your organization.

My professional journey has been characterized by continuous growth and learning in {specialized_skills}. I have gained valuable experience working with {matched_content}, which has equipped me to handle diverse challenges and deliver consistent results. My key achievements include {key_achievements}.

{company}'s {dynamic_content} make you an ideal employer for professionals seeking growth and impact. I am particularly impressed by your commitment to innovation and professional development.

With my background in {key_skills}, I offer {career_aspiration}. I have experience leading projects, collaborating with diverse teams, and delivering solutions that drive business value and customer satisfaction.

{closing_phrase}

{candidate_name}"""
        ]
    
    def extract_job_info(self, job_description: str) -> Dict:
        """Extract key information from job description with enhanced skill matching."""
        if not job_description:
            return {}
        
        job_desc_lower = job_description.lower()
        
        # Extract position with enhanced patterns
        position_patterns = [
            r'(?:hiring|seeking|looking for)\s+(?:a|an)?\s*([^\n]+?(?:engineer|developer|manager|analyst|specialist)[^\n]*)',
            r'(?:software|data|marketing|sales)\s+(?:engineer|developer|manager|analyst|specialist)',
            r'(?:we are|we\'re)\s+(?:looking for|hiring|seeking)\s+(?:a|an)?\s*([^\n]+?(?:engineer|developer|manager|analyst|specialist)[^\n]*)',
            r'(?:Fresher|Junior|Senior|Lead|Principal)\s+([A-Z][a-z]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'([A-Z][a-z]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*\((?:Fresher|Junior|Senior|Lead|Principal)\)',
            # Add pattern for explicit role mention in job description
            r'(?:position|role|title)[:\s]*([^\n]+?(?:engineer|developer|manager|analyst|specialist)[^\n]*)',
            r'(?:for\s+the\s+)([^\n]+?(?:engineer|developer|manager|analyst|specialist)[^\n]*)',
        ]
        
        position = "Professional"
        for pattern in position_patterns:
            match = re.search(pattern, job_description, re.IGNORECASE)
            if match:
                if pattern == r'(?:engineer|developer|manager|analyst|specialist)':
                    position = match.group(1).strip()
                else:
                    position = match.group(1).strip()
                break
        
        # Enhanced skill extraction with role-specific prioritization
        skills = []
        
        # Clean the entire job description first to remove all line breaks
        job_desc_clean = job_description.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ')
        job_desc_lower = job_desc_clean.lower()
        
        # Priority 1: Direct extraction from job description
        skill_patterns = [
            r'expertise in ([^.]+)',
            r'skills in ([^.]+)',
            r'with ([^.]+)',
            r'proficiency in ([^.]+)',
            r'knowledge of ([^.]+)',
            r'experience with ([^.]+)',
            r'requirements?:? ([^.]+)',
            r'seeking ([^.]+)',
            r'looking for ([^.]+)',
            r'including ([^.]+)',
            r'specializing in ([^.]+)',
            r'background in ([^.]+)',
            r'familiar with ([^.]+)',
            r'working knowledge of ([^.]+)'
        ]
        
        for pattern in skill_patterns:
            matches = re.findall(pattern, job_desc_lower)
            for match in matches:
                # Clean up the match and handle line breaks
                cleaned_match = match.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ')
                extracted_skills = [skill.strip() for skill in cleaned_match.split(',')]
                for skill in extracted_skills:
                    skill = skill.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').strip()
                    if skill and len(skill) > 1 and skill not in skills:
                        skills.append(skill)
        
        # Priority 2: Role-specific skill database matching (HIGHEST PRIORITY)
        role_skills = {
            'devops': ['docker', 'kubernetes', 'jenkins', 'ci/cd', 'aws', 'azure', 'terraform', 'ansible'],
            'data scientist': ['python', 'machine learning', 'tensorflow', 'pytorch', 'pandas', 'numpy', 'data analysis', 'statistics'],
            'full stack developer': ['react', 'node.js', 'javascript', 'typescript', 'html', 'css', 'express', 'mongodb'],
            'frontend developer': ['react', 'vue', 'angular', 'javascript', 'typescript', 'html', 'css', 'sass'],
            'backend developer': ['node.js', 'express', 'python', 'java', 'django', 'flask', 'microservices', 'rest api'],
            'mobile developer': ['react native', 'flutter', 'ios', 'android', 'swift', 'kotlin'],
            'ml engineer': ['python', 'tensorflow', 'pytorch', 'scikit-learn', 'machine learning', 'deep learning']
        }
        
        # Add role-specific skills based on position (CLEAR AND REPLACE GENERIC SKILLS)
        position_lower = position.lower()
        role_matched = False
        
        # Check for exact matches first, then partial matches
        for role, role_skill_list in role_skills.items():
            # Exact match first
            if role == position_lower:
                role_matched = True
                skills = []
                for skill in role_skill_list:
                    if len(skills) < 6:
                        skills.append(skill)
                print(f"🔍 Debug: Exact role matched: {role} -> Skills: {skills}")
                break
            # Then check for partial matches
            elif role in position_lower or position_lower in role:
                role_matched = True
                skills = []
                for skill in role_skill_list:
                    if len(skills) < 6:
                        skills.append(skill)
                print(f"🔍 Debug: Partial role matched: {role} -> Skills: {skills}")
                break
            # Finally check for keyword matches
            elif any(keyword in position_lower for keyword in role.split()):
                role_matched = True
                skills = []
                for skill in role_skill_list:
                    if len(skills) < 6:
                        skills.append(skill)
                print(f"🔍 Debug: Keyword role matched: {role} -> Skills: {skills}")
                break
        
        if not role_matched:
            print(f"🔍 Debug: No role matched for position: {position_lower}")
        else:
            print(f"🔍 Debug: Successfully matched role for position: {position_lower}")
        
        # Priority 3: Enhanced database matching (only if no role matched)
        if not role_matched:
            for category, skill_list in self.skill_database.items():
                for skill in skill_list:
                    skill_lower = skill.lower()
                    if (skill_lower in job_desc_lower and 
                        skill_lower not in skills and 
                        len(skills) < 8):
                        skills.append(skill)
        
        # Extract company values
        values_keywords = ['innovation', 'excellence', 'collaboration', 'growth', 'integrity', 'diversity', 'customer focus', 'sustainability']
        company_values = []
        for value in values_keywords:
            if value.lower() in job_desc_lower:
                company_values.append(value)
        
        return {
            'position': position,
            'skills': ', '.join(skills[:6]) if skills else 'relevant technologies',
            'company_values': ', '.join(company_values[:3]) if company_values else 'innovation and excellence'
        }
    
    def extract_job_info_with_target_role(self, job_description: str, target_role: str = "") -> Dict:
        """Extract key information from job description with target role fallback."""
        print(f"🔍 Debug: extract_job_info_with_target_role called with target_role: '{target_role}'")
        
        # First try normal extraction
        job_info = self.extract_job_info(job_description)
        print(f"🔍 Debug: Original job_info position: '{job_info.get('position', 'N/A')}'")
        print(f"🔍 Debug: Original job_info skills: '{job_info.get('skills', 'N/A')}'")
        
        # If no position found or position is generic, use target_role
        if (job_info.get('position', 'Professional') == 'Professional' or 
            'position' not in job_info or 
            not job_info.get('position')) and target_role:
            print(f"🔍 Debug: Using target_role fallback: '{target_role}'")
            job_info['position'] = target_role
            # Re-run role matching with the target role
            position_lower = target_role.lower()
            role_skills = {
                'devops': ['docker', 'kubernetes', 'jenkins', 'ci/cd', 'aws', 'azure', 'terraform', 'ansible'],
                'data scientist': ['python', 'machine learning', 'tensorflow', 'pytorch', 'pandas', 'numpy', 'data analysis', 'statistics'],
                'full stack developer': ['react', 'node.js', 'javascript', 'typescript', 'html', 'css', 'express', 'mongodb'],
                'frontend developer': ['react', 'vue', 'angular', 'javascript', 'typescript', 'html', 'css', 'sass'],
                'backend developer': ['node.js', 'express', 'python', 'java', 'django', 'flask', 'microservices', 'rest api'],
                'mobile developer': ['react native', 'flutter', 'ios', 'android', 'swift', 'kotlin'],
                'ml engineer': ['python', 'tensorflow', 'pytorch', 'scikit-learn', 'machine learning', 'deep learning']
            }
            
            print(f"🔍 Debug: Checking role matching for position_lower: '{position_lower}'")
            for role, role_skill_list in role_skills.items():
                if role in position_lower or position_lower in role or any(keyword in position_lower for keyword in role.split()):
                    print(f"🔍 Debug: Role matched! {role} -> {role_skill_list}")
                    job_info['skills'] = ', '.join(role_skill_list[:6])
                    break
            else:
                print(f"🔍 Debug: No role matched for '{position_lower}'")
        
        print(f"🔍 Debug: Final job_info position: '{job_info.get('position', 'N/A')}'")
        print(f"🔍 Debug: Final job_info skills: '{job_info.get('skills', 'N/A')}'")
        return job_info
    
    def extract_user_info(self, user_input: str, job_info: Dict = None) -> Dict:
        """Extract key information from user input."""
        if not user_input:
            return {}
        
        # Extract name (improved heuristic)
        name_patterns = [
            # Name after years enhancement (web server format)
            r'I have \d+ years of experience\.?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            # Name at very beginning (resume format) - first line only
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            # Explicit name statements
            r'(?:my name is|i am|i\'m)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:is|am|have|possess)',
            # Name label pattern (for resume format)
            r'Name[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            # Name at beginning of input
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*[,.]?\s*(?:have|am|with|experienced)',
            # Name with experience patterns
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:with|having)\s+\d+\s*(?:years?|yrs?)',
            # Simple name followed by skills
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*[,-]?\s*(?:experienced|skilled|proficient)',
            # Name followed by numbers (years of experience)
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+\d+',
            # Just a name at the start (fallback)
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
        ]
        
        name = "Candidate"
        print(f"🔍 Debug: Extracting name from user_input: {user_input[:200]}...")
        for i, pattern in enumerate(name_patterns):
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                extracted_name = match.group(1).strip()
                print(f"🔍 Debug: Pattern {i+1} matched: {extracted_name}")
                # Validate that it looks like a real name (2+ letters, starts with capital)
                if len(extracted_name) >= 2 and extracted_name[0].isupper():
                    name = extracted_name
                    print(f"🔍 Debug: Name extracted successfully: {name}")
                    break
                else:
                    print(f"🔍 Debug: Name validation failed: {extracted_name}")
            else:
                print(f"🔍 Debug: Pattern {i+1} no match: {pattern}")
        
        print(f"🔍 Debug: Final name result: {name}")
        
        # Extract experience - improved patterns
        experience_patterns = [
            r'(\d+)\s*(?:years?|yr)s?\s*(?:of\s*)?(?:experience|exp)',
            r'(\d+)\s*\+\s*(?:years?|yr)s?\s*(?:of\s*)?(?:experience|exp)',
            r'(?:experience|exp)[:\s]+(\d+)\s*(?:years?|yr)s?',
            r'(\d+)\s*(?:years?|yr)s?\s*(?:of\s*)?(?:professional|work|software)',
            r'(?:have|with|possess)\s+(\d+)\s*(?:years?|yr)s?',
            r'(\d+)\s*(?:years?|yr)s?\s+(?:of\s*)?(?:experience|exp|work|practice)',
            # Comma-separated format: "Nil,4 years,skills"
            r'[,\s]+(\d+)\s*(?:years?|yr)s?'
        ]
        
        years = "0 years"
        for pattern in experience_patterns:
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                years = match.group(1) + " years"
                print(f"🔍 Debug: Experience extracted - Pattern: {pattern}, Match: {match.group(1)}, Years: {years}")
                break
        else:
            print(f"🔍 Debug: No experience found in user_input: {user_input[:100]}...")
        
        # Extract skills - prioritize job-specific skills from job_info
        skills = []
        
        # Clean user input completely to remove all line breaks and extra spaces
        user_input_clean = user_input.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').replace('   ', ' ')
        user_input_lower = user_input_clean.lower()
        job_skills_lower = job_info.get('skills', '').lower() if job_info else ''
        
        # Remove ALL experience phrases from user input to avoid false skill matches
        cleaned_input = user_input_lower
        cleaned_input = re.sub(r'\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', cleaned_input)
        cleaned_input = re.sub(r'\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+in', '', cleaned_input)
        cleaned_input = re.sub(r'with\s+\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', cleaned_input)
        cleaned_input = re.sub(r'building\s+comprehensive\s+skills\s+in\s+\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', cleaned_input)
        cleaned_input = re.sub(r'focused\s+on\s+building\s+comprehensive\s+skills\s+in\s+\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', cleaned_input)
        cleaned_input = re.sub(r'characterized\s+by\s+continuous\s+growth\s+and\s+learning\s+in\s+\d+\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', cleaned_input)
        
        # Additional cleaning to remove any remaining line breaks or weird spacing
        cleaned_input = re.sub(r'\s+', ' ', cleaned_input)  # Normalize all whitespace
        cleaned_input = cleaned_input.replace('deployingai', 'deploying ai')  # Fix specific "deployingai" issue
        cleaned_input = cleaned_input.replace('deploying ', 'deploying')  # Fix specific "deploying" gap issue
        cleaned_input = cleaned_input.replace('deploying  ', 'deploying')  # Fix double spaces after deploying
        
        # Debug logging (comment out in production)
        # print(f"🔍 Debug: Original user_input: {user_input[:200]}...")
        # print(f"🔍 Debug: Cleaned input for skills: {cleaned_input[:200]}...")
        # print(f"🔍 Debug: Job skills: {job_skills_lower}")
        
        # Extract job skills first (highest priority)
        job_skill_list = [skill.strip().lower() for skill in job_skills_lower.split(',') if skill.strip()]
        
        # Add job-specific skills that match user input
        for job_skill in job_skill_list:
            if job_skill in cleaned_input and job_skill not in skills:
                skills.append(job_skill)
        
        # Extract user skills from input (secondary priority)
        user_skill_patterns = [
            r'experience in ([^.]+)',
            r'skilled in ([^.]+)',
            r'proficient in ([^.]+)',
            r'knowledge of ([^.]+)',
            r'expertise in ([^.]+)',
            r'background in ([^.]+)',
            r'foundation in ([^.]+)'
        ]
        
        user_skills_found = []
        for pattern in user_skill_patterns:
            matches = re.findall(pattern, cleaned_input)
            for match in matches:
                extracted_skills = [skill.strip().lower() for skill in match.split(',')]
                for skill in extracted_skills:
                    if skill and len(skill) > 1 and skill not in user_skills_found:
                        user_skills_found.append(skill)
        
        # Add user skills that match job requirements
        for user_skill in user_skills_found:
            if user_skill not in skills and len(skills) < 5:
                # Check if user skill relates to any job skill
                job_related = any(
                    user_skill in job_skill or 
                    job_skill in user_skill or
                    any(word in user_skill for word in job_skill.split()) or
                    any(word in job_skill for word in user_skill.split())
                    for job_skill in job_skill_list
                )
                if job_related or len(skills) < 3:  # Add if job-related or need more skills
                    skills.append(user_skill)
        
        # Then extract from skill database (fallback)
        for category, skill_list in self.skill_database.items():
            for skill in skill_list:
                skill_lower = skill.lower()
                if (skill_lower in cleaned_input and 
                    skill_lower not in skills and 
                    not any(exp_phrase in cleaned_input for exp_phrase in [
                        f'{skill_lower} years', f'years {skill_lower}', 
                        f'experience {skill_lower}', f'{skill_lower} experience',
                        f'developing robust solutions with {skill_lower}',
                        f'professional experience developing robust solutions with {skill_lower}'
                    ]) and len(skills) < 5):
                    # print(f"🔍 Debug: Skill found: {skill}")
                    skills.append(skill)
        
        # Extract achievements
        achievement_keywords = ['developed', 'created', 'implemented', 'led', 'managed', 'achieved', 'improved', 'optimized']
        achievements = []
        for keyword in achievement_keywords:
            if keyword.lower() in user_input.lower():
                achievements.append(keyword)
        
        return {
            'name': name,
            'years': years,
            'skills': ', '.join([skill.replace('\n', ' ').replace('\r', ' ').strip() for skill in skills[:5]]) if skills else 'relevant technologies',
            'achievements': ', '.join([achievement.replace('\n', ' ').replace('\r', ' ').strip() for achievement in achievements[:3]]) if achievements else 'delivering successful projects',
            'experience_level': self._determine_experience_level(years)
        }
    
    def debug_extract_user_info(self, user_input: str) -> Dict:
        """Debug version to see what's being extracted."""
        result = self.extract_user_info(user_input)
        print(f"🔍 Generator Debug - Extracted: {result}")
        return result
    
    def _determine_experience_level(self, years: str) -> str:
        """Determine experience level from years string."""
        try:
            years_num = int(re.findall(r'\d+', years)[0])
            if years_num < 2:
                return 'fresher'
            elif years_num < 5:
                return 'mid-level'
            else:
                return 'experienced'
        except:
            return 'mid-level'
    
    def _determine_tone(self, job_info: Dict, user_info: Dict) -> str:
        """Determine appropriate tone based on context."""
        if not job_info or not user_info:
            return 'professional'
        
        # Analyze job description for tone indicators
        jd_lower = str(job_info).lower()
        
        if any(word in jd_lower for word in ['innovative', 'dynamic', 'fast-paced', 'startup']):
            return 'enthusiastic'
        elif any(word in jd_lower for word in ['corporate', 'enterprise', 'formal', 'professional']):
            return 'formal'
        else:
            return 'professional'
    
    def _generate_dynamic_content(self, job_info: Dict, user_info: Dict, content_type: str = "general") -> str:
        """Generate dynamic content based on context and content type with true randomness."""
        if not job_info or not user_info:
            return "professional growth and development"
        
        # Use time-based seed with microsecond precision and additional entropy for true randomness
        import os
        entropy_source = int(time.time() * 1000000) + os.getpid() + int.from_bytes(os.urandom(4), 'big')
        random.seed(entropy_source)
        
        company = job_info.get('company', 'the company')
        user_skills = user_info.get('skills', '').lower()
        experience_level = user_info.get('experience_level', 'mid-level')
        user_years = user_info.get('years', '0 years')
        
        # Dynamic content generation based on type
        if content_type == "company_alignment":
            company_content = [
                f"your innovative approach to emerging technologies and digital transformation",
                f"your commitment to excellence and pushing technological boundaries",
                f"your focus on creating meaningful impact through cutting-edge solutions",
                f"your dedication to solving complex challenges with innovative approaches",
                f"your culture of continuous learning and professional growth",
                f"your vision for transforming the industry through technology",
                f"your emphasis on quality, user experience, and scalable solutions",
                f"your leadership in the technology sector",
                f"your reputation for delivering breakthrough innovations",
                f"your forward-thinking approach to technological advancement",
                f"your excellence in developing next-generation solutions"
            ]
            return random.choice(company_content)
        
        elif content_type == "value_proposition":
            if experience_level == 'fresher':
                value_content = [
                    f"my fresh perspective combined with strong theoretical foundations",
                    f"my enthusiasm for learning and adapting to new technologies",
                    f"my academic excellence and practical project experience",
                    f"my ability to bring new ideas and energy to established teams",
                    f"my strong foundation in modern development practices"
                ]
            elif experience_level == 'mid-level':
                value_content = [
                    f"my proven ability to bridge technical solutions with business needs",
                    f"my experience in both individual contributions and team leadership",
                    f"my track record of delivering projects on time and exceeding expectations",
                    f"my expertise in scaling applications and optimizing performance",
                    f"my experience in leading cross-functional teams to success"
                ]
            else:  # experienced
                value_content = [
                    f"my extensive background in system architecture and strategic planning",
                    f"my leadership experience in mentoring teams and driving innovation",
                    f"my proven ability to transform business requirements into technical solutions",
                    f"my expertise in enterprise-level development and best practices",
                    f"my track record of successful project delivery and team building"
                ]
            return random.choice(value_content)
        
        elif content_type == "career_aspiration":
            career_content = [
                f"contributing to {company}'s mission of technological excellence",
                f"growing professionally while delivering value to your organization",
                f"applying my skills to solve meaningful challenges at {company}",
                f"becoming an integral part of your innovative team",
                f"advancing my career while helping {company} achieve its goals",
                f"leveraging my expertise to drive {company}'s success",
                f"making a lasting impact through technical excellence and innovation",
                f"building a future together through collaboration and shared success"
            ]
            return random.choice(career_content)
        
        elif content_type == "skills_demonstration":
            user_skill_list = [skill.strip() for skill in user_info.get('skills', '').split(',') if skill.strip()]
            if user_skill_list:
                skill_content = [
                    f"my hands-on experience with {', '.join(user_skill_list[:3])} in real-world projects",
                    f"my proven track record of delivering solutions using {', '.join(user_skill_list[:3])}",
                    f"my expertise in developing robust applications with {', '.join(user_skill_list[:3])}",
                    f"my comprehensive understanding of {', '.join(user_skill_list[:3])} and best practices",
                    f"my ability to leverage {', '.join(user_skill_list[:3])} to solve complex business problems"
                ]
                return random.choice(skill_content)
            else:
                general_skills = ["modern technologies", "innovative solutions", "scalable systems", "best practices"]
                return random.choice(general_skills)
        
        else:  # general content
            general_content = [
                "professional growth and development",
                "innovative technology solutions", 
                "scalable system architecture",
                "cutting-edge development practices",
                "business-driven technology solutions",
                "enterprise-level software development",
                "strategic technical innovation",
                "continuous learning and skill advancement"
            ]
            return random.choice(general_content)
            return "professional growth and development"
        
        user_skills = user_info.get('skills', '').lower()
        job_skills = job_info.get('skills', '').lower()
        user_years = user_info.get('years', '0 years')
        experience_level = user_info.get('experience_level', 'mid-level')
        company = job_info.get('company', 'the company')
        position = job_info.get('position', 'this position')
        
        # Find common skills
        common_skills = []
        if user_skills and job_skills:
            user_skill_list = [skill.strip().lower() for skill in user_skills.split(',')]
            job_skill_list = [skill.strip().lower() for skill in job_skills.split(',')]
            common_skills = list(set(user_skill_list) & set(job_skill_list))
        
        # Dynamic content based on content type
        if content_type == "company_alignment":
            company_content = [
                f"your innovative approach to emerging technologies and digital transformation",
                f"your commitment to excellence and pushing technological boundaries",
                f"your focus on creating meaningful impact through cutting-edge solutions",
                f"your dedication to solving complex challenges with innovative approaches",
                f"your culture of continuous learning and professional growth",
                f"your vision for transforming the industry through technology",
                f"your emphasis on quality, user experience, and scalable solutions",
                f"your leadership in the technology sector",
                f"your reputation for delivering breakthrough innovations",
                f"your forward-thinking approach to technological advancement",
                f"your excellence in developing next-generation solutions"
            ]
            return random.choice(company_content)
        
        elif content_type == "skills_demonstration":
            if common_skills:
                skill_content = [
                    f"my hands-on experience with {', '.join(common_skills[:3])} in real-world projects",
                    f"my proven track record of delivering solutions using {', '.join(common_skills[:3])}",
                    f"my expertise in developing robust applications with {', '.join(common_skills[:3])}",
                    f"my comprehensive understanding of {', '.join(common_skills[:3])} and best practices",
                    f"my ability to leverage {', '.join(common_skills[:3])} to solve complex business problems"
                ]
                return random.choice(skill_content)
            else:
                fallback_skills = ["modern technologies", "innovative solutions", "scalable systems", "best practices", "cutting-edge development", "advanced problem-solving", "strategic technical thinking"]
                return random.choice(fallback_skills)
        
        elif content_type == "value_proposition":
            if experience_level == 'fresher':
                value_content = [
                    "my fresh perspective combined with strong theoretical foundations",
                    "my enthusiasm for learning and adapting to new technologies",
                    "my academic excellence and practical project experience",
                    "my ability to bring new ideas and energy to established teams",
                    "my strong foundation in modern development practices"
                ]
            elif experience_level == 'mid-level':
                value_content = [
                    f"my {user_years} of balanced technical and business experience",
                    "my proven ability to bridge technical solutions with business needs",
                    "my experience in both individual contributions and team leadership",
                    "my track record of delivering projects on time and exceeding expectations",
                    "my expertise in scaling applications and optimizing performance"
                ]
            else:  # experienced
                value_content = [
                    "my extensive background in system architecture and strategic planning",
                    "my leadership experience in mentoring teams and driving innovation",
                    "my proven ability to transform business requirements into technical solutions",
                    "my expertise in enterprise-level development and best practices",
                    "my track record of successful project delivery and team building"
                ]
            return random.choice(value_content)
        
        elif content_type == "career_aspiration":
            aspiration_content = [
                f"contributing to {company}'s mission of technological excellence",
                f"growing professionally while delivering value to your organization",
                f"applying my skills to solve meaningful challenges at {company}",
                f"becoming an integral part of your innovative team",
                f"advancing my career while helping {company} achieve its goals",
                f"leveraging my expertise to drive {company}'s success",
                f"making a lasting impact through technical excellence and innovation",
                f"building a future together through collaboration and shared success"
            ]
            return random.choice(aspiration_content)
        
        else:  # general content
            if common_skills:
                return f"expertise in {', '.join(common_skills[:3])}"
            else:
                general_content = [
                    "professional growth and development",
                    "innovative technology solutions",
                    "scalable system architecture",
                    "cutting-edge development practices",
                    "business-driven technology solutions",
                    "enterprise-level software development",
                    "strategic technical innovation",
                    "continuous learning and skill advancement"
                ]
                return random.choice(general_content)
    
    def _enhance_natural_flow(self, text: str) -> str:
        """Enhance natural flow and readability."""
        # Remove repetitive phrases
        text = re.sub(r'\b(I am|I have|I believe)\s+\1+', r'\1', text, flags=re.IGNORECASE)
        
        # Clean up trailing 'and' in signatures and other places
        text = re.sub(r'([A-Z][a-z\s]+)\s+and\s*$', r'\1', text, flags=re.MULTILINE)
        text = re.sub(r'([A-Z][a-z]+)\s+and\s*$', r'\1', text, flags=re.MULTILINE)
        
        # Remove duplicate closing sentences
        lines = text.split('\n')
        cleaned_lines = []
        seen_lines = set()
        
        for line in lines:
            line = line.strip()
            if line and line not in seen_lines:
                cleaned_lines.append(line)
                seen_lines.add(line)
            elif not line:  # Keep empty lines for paragraph breaks
                cleaned_lines.append(line)
        
        text = '\n'.join(cleaned_lines)
        
        # Only add transitions where appropriate (not too many)
        # This was adding too many "Additionally" - let's remove it for now
        # text = re.sub(r'\. ([A-Z])', r'. Additionally, \1', text)
        
        return text
    
    def _clean_generated_text(self, text: str) -> str:
        """Clean and format generated text."""
        # First, preserve all newlines by temporarily replacing them
        text = text.replace('\n\n', '<<PARAGRAPH_BREAK>>')
        text = text.replace('\n', '<<LINE_BREAK>>')
        
        # Remove extra whitespace but preserve paragraph breaks
        # Replace multiple spaces with single space
        text = re.sub(r' +', ' ', text)
        
        # Restore paragraph breaks first, then line breaks
        text = text.replace('<<PARAGRAPH_BREAK>>', '\n\n')
        text = text.replace('<<LINE_BREAK>>', '\n')
        
        # Clean up any extra spaces around newlines
        text = re.sub(r' \n', '\n', text)
        text = re.sub(r'\n ', '\n', text)
        
        # Fix common text issues
        text = re.sub(r'\b(for for|the the|and and|in in)\b', lambda m: m.group(0).split()[0], text, flags=re.IGNORECASE)
        
        # Ensure proper spacing around punctuation, but preserve paragraphs
        # First preserve paragraphs
        text = text.replace('\n\n', '<<TEMP_PARAGRAPH>>')
        text = re.sub(r'\s*([,.!?])\s*', r'\1 ', text)
        text = text.replace('<<TEMP_PARAGRAPH>>', '\n\n')
        
        # Remove duplicate sentences while preserving paragraphs
        # Split into paragraphs first
        paragraphs = text.split('\n\n')
        unique_paragraphs = []
        
        for paragraph in paragraphs:
            # Process each paragraph for duplicate sentences
            sentences = paragraph.split('. ')
            unique_sentences = []
            seen = set()
            
            for sentence in sentences:
                sentence = sentence.strip()
                if sentence and sentence not in seen:
                    unique_sentences.append(sentence)
                    seen.add(sentence)
            
            # Reconstruct the paragraph
            reconstructed_paragraph = '. '.join(unique_sentences)
            unique_paragraphs.append(reconstructed_paragraph)
        
        # Rejoin paragraphs
        return '\n\n'.join(unique_paragraphs)
    
    def generate_cover_letter(self, job_description: str, user_input: str, 
                            best_match_content: str = "", company: str = "", experience_level: str = "", target_role: str = "") -> str:
        """Generate a personalized cover letter."""
        # Use enhanced job info extraction with target_role fallback
        job_info = self.extract_job_info_with_target_role(job_description, target_role)
        user_info = self.extract_user_info(user_input, job_info)
        
        # Determine experience level if not provided
        if not experience_level:
            experience_level = user_info.get('experience_level', 'mid-level')
        
        # Select appropriate template based on user context and skills
        templates = self.templates.get(experience_level, self.templates['mid-level'])
        
        # Intelligent template selection based on user context
        user_skills_lower = user_info.get('skills', '').lower()
        user_name = user_info.get('name', 'Candidate')
        
        # Select template based on skills and context
        if 'python' in user_skills_lower and 'django' in user_skills_lower:
            template = templates[0]  # Backend-focused template
        elif 'react' in user_skills_lower or 'vue' in user_skills_lower:
            template = templates[1] if len(templates) > 1 else templates[0]  # Frontend-focused
        elif 'machine learning' in user_skills_lower or 'tensorflow' in user_skills_lower:
            template = templates[-1]  # ML-focused template
        else:
            # Use hash of user skills for consistent but varied selection
            skill_hash = hash(user_skills_lower + user_name) % len(templates)
            template = templates[skill_hash]
        
        # Determine tone
        tone = self._determine_tone(job_info, user_info)
        
        # Process user skills into intelligent narrative
        user_skills = user_info.get('skills', 'relevant technologies')
        if 'go' in user_skills.lower():
            skills_list = [skill for skill in user_skills.split(',') if skill.strip().lower() != 'go']
            user_skills = ', '.join(skills_list) if skills_list else 'relevant technologies'
        
        # Create skill narrative based on experience level and skill combination
        skill_narrative = self._create_skill_narrative(user_info.get('skills', ''), experience_level, user_info.get('years', '0 years'))
        
        # Shuffle skills for variety but maintain narrative coherence
        skills_list = [skill.strip() for skill in user_skills.split(',')]
        if len(skills_list) > 4:
            # Group related skills for better flow
            grouped_skills = self._group_related_skills(skills_list)
            user_skills = ', '.join(grouped_skills[:6])
        
        # Clean up skills to avoid duplicate experience mentions and repetitive phrases
        user_skills = re.sub(r'\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+in', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'with\s+\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'building\s+comprehensive\s+skills\s+in\s+\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'focused\s+on\s+building\s+comprehensive\s+skills\s+in\s+\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'characterized\s+by\s+continuous\s+growth\s+and\s+learning\s+in\s+\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'strong\s+foundation\s+in\s+([^.]+)\s+with\s+academic\s+projects\s+demonstrating\s+practical\s+application', r'\1', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'extensive\s+background\s+in\s+([^.]+)\s+with\s+expertise\s+in\s+system\s+architecture\s+and\s+optimization', r'\1', user_skills, flags=re.IGNORECASE)
        user_skills = re.sub(r'\s+', ' ', user_skills).strip()
        if not user_skills:
            user_skills = 'python, java, javascript, c++, flask'
        
        # Clean up skill narrative as well
        if 'skill_narrative' in locals():
            skill_narrative = re.sub(r'\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+developing\s+robust\s+solutions\s+with', '', skill_narrative, flags=re.IGNORECASE)
            skill_narrative = re.sub(r'\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience\s+in', '', skill_narrative, flags=re.IGNORECASE)
            skill_narrative = re.sub(r'strong\s+foundation\s+in\s+([^.]+)\s+with\s+academic\s+projects\s+demonstrating\s+practical\s+application', r'\1', skill_narrative, flags=re.IGNORECASE)
            skill_narrative = re.sub(r'extensive\s+background\s+in\s+([^.]+)\s+with\s+expertise\s+in\s+system\s+architecture\s+and\s+optimization', r'\1', skill_narrative, flags=re.IGNORECASE)
            skill_narrative = re.sub(r'\s+', ' ', skill_narrative).strip()
        
        # Prepare template variables with role-specific skills and randomization
        import os
        entropy_source = int(time.time() * 1000000) + os.getpid() + int.from_bytes(os.urandom(4), 'big')
        random.seed(entropy_source)  # Use microseconds + PID + random bytes for true randomness
        
        # Generate multiple dynamic content elements for true variety
        dynamic_company_alignment = self._generate_dynamic_content(job_info, user_info, "company_alignment")
        dynamic_value_proposition = self._generate_dynamic_content(job_info, user_info, "value_proposition")
        dynamic_career_aspiration = self._generate_dynamic_content(job_info, user_info, "career_aspiration")
        dynamic_skills_demonstration = self._generate_dynamic_content(job_info, user_info, "skills_demonstration")
        
        # Create role-specific skill narrative
        user_skills_list = user_info.get('skills', '').split(', ') if user_info.get('skills') else []
        if user_skills_list:
            skill_narrative = f"proficiency in {', '.join(user_skills_list[:4])}"
        else:
            skill_narrative = job_info.get('skills', user_skills)
        
        template_vars = {
            'hiring_manager': 'Hiring Manager',
            'position': target_role or job_info.get('position', 'Professional position'),
            'company': company or job_info.get('company', 'the Company'),
            'key_skills': skill_narrative,  # Now role-specific
            'matched_content': dynamic_skills_demonstration,  # Use dynamic content
            'years_experience': user_info.get('years', '0 years'),
            'candidate_name': user_info.get('name', 'Candidate'),
            'company_values': job_info.get('company_values', 'innovation and excellence'),
            'key_achievements': user_info.get('achievements', 'delivering successful projects'),
            'professional_values': 'professional excellence',
            'specialized_skills': skill_narrative,  # Now role-specific
            'opening_phrase': random.choice(self.opening_phrases),
            'closing_phrase': random.choice(self.closing_phrases),
            'dynamic_content': dynamic_company_alignment,  # Add dynamic content
            'value_proposition': dynamic_value_proposition,  # Add value proposition
            'career_aspiration': dynamic_career_aspiration,  # Add career aspiration
        }
        
        # Determine tone for the cover letter
        tone = self._determine_tone(job_info, user_info)
        
        # Add additional dynamic content variables
        template_vars.update({
            'tone': tone,
            'dynamic_content': dynamic_company_alignment,
            'value_proposition': dynamic_value_proposition,
            'career_aspiration': dynamic_career_aspiration
        })
        
        try:
            # Generate cover letter
            cover_letter = template.format(**template_vars)
            
            # Aggressive cleanup for duplicate experience mentions
            # Remove patterns like "3 years of experience in 3 years of professional experience"
            cover_letter = re.sub(r'(\d+\+?\s*years?\s+of\s+experience)\s+in\s+(\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience)', r'\1', cover_letter, flags=re.IGNORECASE)
            cover_letter = re.sub(r'With\s+(\d+\+?\s*years?\s+of\s+experience)\s+in\s+(\d+\+?\s*years?\s+(?:of\s+)?(?:professional\s+)?experience)', r'With \1', cover_letter, flags=re.IGNORECASE)
            
            # Fix duplicate experience mentions - only replace if needed
            user_years = user_info.get('years', '3 years')
            if user_years != '3 years':
                # Replace the experience in the generated letter with the correct one
                cover_letter = re.sub(r'\b\d+\+?\s*years?\s+of\s+experience', user_years + ' of experience', cover_letter, flags=re.IGNORECASE)
                cover_letter = re.sub(r'\b\d+\+?\s*years?\s+professional\s+experience', user_years + ' professional experience', cover_letter, flags=re.IGNORECASE)
            
            # Enhance and clean
            cover_letter = self._enhance_natural_flow(cover_letter)
            cover_letter = self._clean_generated_text(cover_letter)
            
            # Final cleanup - remove trailing 'and' from signature
            cover_letter = re.sub(r'([A-Z][a-z\s]+)\s+and\s*$', r'\1', cover_letter, flags=re.MULTILINE)
            cover_letter = re.sub(r'([A-Z][a-z]+)\s+and\s*$', r'\1', cover_letter, flags=re.MULTILINE)
            
            # Aggressive cleanup for any trailing 'and' after names
            lines = cover_letter.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                # Check if line looks like a name (2+ words, starts with capital letters)
                if re.match(r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+', line):
                    # Remove trailing 'and'
                    line = re.sub(r'\s+and\s*$', '', line)
                    lines[i] = line
            
            cover_letter = '\n'.join(lines)
            
            # Ultimate cleanup - remove 'and' from the very end of the document
            cover_letter = cover_letter.rstrip()
            if cover_letter.endswith(' and'):
                cover_letter = cover_letter[:-4].rstrip()
            elif cover_letter.endswith(' and '):
                cover_letter = cover_letter[:-5].rstrip()
            
            return cover_letter
            
        except Exception as e:
            # Fallback cover letter
            return f"""Dear Hiring Manager,

I am excited to apply for the {template_vars['position']} position at {template_vars['company'] or 'your company'}.
Based on my background in {user_info.get('skills', 'relevant technologies')} and the requirements outlined in your job description, I believe I would be a valuable addition to your team.

I look forward to discussing how my qualifications can benefit your organization.

Thank you for your consideration.

Sincerely,
{user_info.get('name', 'Candidate')}"""
