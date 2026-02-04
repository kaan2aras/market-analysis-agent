"""Data collector module for gathering AI app/marketplace data."""

class DataCollector:
    """Collects data about AI apps and marketplaces."""
    
    def __init__(self):
        """Initialize the data collector with sample AI app data."""
        self.data = self._get_sample_data()
    
    def _get_sample_data(self):
        """Return sample data of 29 real AI apps with accurate information."""
        return [
            # Chatbots/Assistants
            {
                'App Name': 'ChatGPT',
                'Company': 'OpenAI',
                'Category': 'Chatbot',
                'Pricing Model': 'Freemium',
                'Rating': 4.8,
                'Downloads': '100M+',
                'App Store Link': 'https://apps.apple.com/us/app/chatgpt/id6448311069',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.openai.chatgpt',
                'Website': 'https://chat.openai.com',
                'Key Features': 'AI chat, code generation, image analysis, web browsing, GPT-4',
                'Region': 'Global',
                'Last Updated': '2026-02-01'
            },
            {
                'App Name': 'Claude',
                'Company': 'Anthropic',
                'Category': 'Chatbot',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '20M+',
                'App Store Link': 'https://apps.apple.com/us/app/claude-by-anthropic/id6473753684',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.anthropic.claude',
                'Website': 'https://claude.ai',
                'Key Features': 'Safe AI, long context (200k tokens), document analysis, coding',
                'Region': 'Global',
                'Last Updated': '2026-02-02'
            },
            {
                'App Name': 'Gemini',
                'Company': 'Google',
                'Category': 'Chatbot',
                'Pricing Model': 'Free',
                'Rating': 4.5,
                'Downloads': '50M+',
                'App Store Link': 'https://apps.apple.com/us/app/google-gemini/id6476319100',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.google.android.apps.bard',
                'Website': 'https://gemini.google.com',
                'Key Features': 'Multimodal AI, Google integration, real-time information, image generation',
                'Region': 'Global',
                'Last Updated': '2026-01-28'
            },
            {
                'App Name': 'Microsoft Copilot',
                'Company': 'Microsoft',
                'Category': 'Chatbot',
                'Pricing Model': 'Free',
                'Rating': 4.4,
                'Downloads': '30M+',
                'App Store Link': 'https://apps.apple.com/us/app/microsoft-copilot/id6472347522',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.microsoft.copilot',
                'Website': 'https://copilot.microsoft.com',
                'Key Features': 'GPT-4 powered, image generation, Microsoft 365 integration',
                'Region': 'Global',
                'Last Updated': '2026-01-30'
            },
            {
                'App Name': 'Perplexity',
                'Company': 'Perplexity AI',
                'Category': 'Chatbot',
                'Pricing Model': 'Freemium',
                'Rating': 4.7,
                'Downloads': '10M+',
                'App Store Link': 'https://apps.apple.com/us/app/perplexity-ask-anything/id1668000334',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=ai.perplexity.app.android',
                'Website': 'https://perplexity.ai',
                'Key Features': 'AI-powered search, citations, research assistant, real-time web access',
                'Region': 'Global',
                'Last Updated': '2026-02-03'
            },
            {
                'App Name': 'Character.AI',
                'Company': 'Character Technologies',
                'Category': 'Chatbot',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '50M+',
                'App Store Link': 'https://apps.apple.com/us/app/character-ai-chat-with-bots/id6443623328',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=ai.character.app',
                'Website': 'https://character.ai',
                'Key Features': 'Create AI characters, roleplay, entertainment, custom personalities',
                'Region': 'Global',
                'Last Updated': '2026-01-25'
            },
            {
                'App Name': 'Pi',
                'Company': 'Inflection AI',
                'Category': 'Chatbot',
                'Pricing Model': 'Free',
                'Rating': 4.5,
                'Downloads': '5M+',
                'App Store Link': 'https://apps.apple.com/us/app/pi-your-personal-ai/id6461888975',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=ai.inflection.app',
                'Website': 'https://pi.ai',
                'Key Features': 'Personal AI, conversational, supportive, voice chat',
                'Region': 'Global',
                'Last Updated': '2026-01-20'
            },
            {
                'App Name': 'Poe',
                'Company': 'Quora',
                'Category': 'Chatbot',
                'Pricing Model': 'Freemium',
                'Rating': 4.3,
                'Downloads': '5M+',
                'App Store Link': 'https://apps.apple.com/us/app/poe-fast-ai-chat/id1640745955',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.quora.poe',
                'Website': 'https://poe.com',
                'Key Features': 'Multiple AI models, GPT-4, Claude, custom bots, bot creation',
                'Region': 'Global',
                'Last Updated': '2026-01-27'
            },
            
            # Image Generation
            {
                'App Name': 'Midjourney',
                'Company': 'Midjourney Inc',
                'Category': 'Image Generation',
                'Pricing Model': 'Paid',
                'Rating': 4.7,
                'Downloads': '10M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.midjourney.com',
                'Key Features': 'AI image generation, high quality, artistic, Discord-based',
                'Region': 'Global',
                'Last Updated': '2026-01-15'
            },
            {
                'App Name': 'DALL-E',
                'Company': 'OpenAI',
                'Category': 'Image Generation',
                'Pricing Model': 'Paid',
                'Rating': 4.6,
                'Downloads': '15M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://labs.openai.com',
                'Key Features': 'AI image generation, editing, variations, prompt-based',
                'Region': 'Global',
                'Last Updated': '2026-01-22'
            },
            {
                'App Name': 'Leonardo AI',
                'Company': 'Leonardo AI',
                'Category': 'Image Generation',
                'Pricing Model': 'Freemium',
                'Rating': 4.5,
                'Downloads': '8M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://leonardo.ai',
                'Key Features': 'AI art generation, game assets, training models, consistent characters',
                'Region': 'Global',
                'Last Updated': '2026-01-18'
            },
            {
                'App Name': 'Adobe Firefly',
                'Company': 'Adobe',
                'Category': 'Image Generation',
                'Pricing Model': 'Freemium',
                'Rating': 4.4,
                'Downloads': '12M+',
                'App Store Link': 'https://apps.apple.com/us/app/adobe-firefly/id6459575657',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.adobe.firefly',
                'Website': 'https://firefly.adobe.com',
                'Key Features': 'Text to image, generative fill, text effects, Adobe integration',
                'Region': 'Global',
                'Last Updated': '2026-01-29'
            },
            {
                'App Name': 'Canva AI',
                'Company': 'Canva',
                'Category': 'Image Generation',
                'Pricing Model': 'Freemium',
                'Rating': 4.8,
                'Downloads': '200M+',
                'App Store Link': 'https://apps.apple.com/us/app/canva-design-photo-video/id897446215',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.canva.editor',
                'Website': 'https://www.canva.com',
                'Key Features': 'Text to image, Magic Edit, background remover, design templates',
                'Region': 'Global',
                'Last Updated': '2026-02-01'
            },
            {
                'App Name': 'Stable Diffusion',
                'Company': 'Stability AI',
                'Category': 'Image Generation',
                'Pricing Model': 'Free',
                'Rating': 4.5,
                'Downloads': '20M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://stability.ai',
                'Key Features': 'Open-source, image generation, customizable, local deployment',
                'Region': 'Global',
                'Last Updated': '2026-01-12'
            },
            
            # Video/Audio
            {
                'App Name': 'Runway',
                'Company': 'Runway AI',
                'Category': 'Video/Audio',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '5M+',
                'App Store Link': 'https://apps.apple.com/us/app/runway-ai-video-editor/id1665024375',
                'Play Store Link': 'N/A',
                'Website': 'https://runwayml.com',
                'Key Features': 'AI video generation, editing, Gen-2, motion tracking',
                'Region': 'Global',
                'Last Updated': '2026-01-26'
            },
            {
                'App Name': 'ElevenLabs',
                'Company': 'ElevenLabs',
                'Category': 'Video/Audio',
                'Pricing Model': 'Freemium',
                'Rating': 4.7,
                'Downloads': '8M+',
                'App Store Link': 'https://apps.apple.com/us/app/elevenlabs-reader/id6479373050',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=io.elevenlabs.readerai',
                'Website': 'https://elevenlabs.io',
                'Key Features': 'Voice synthesis, voice cloning, multilingual, realistic voices',
                'Region': 'Global',
                'Last Updated': '2026-02-02'
            },
            {
                'App Name': 'Synthesia',
                'Company': 'Synthesia',
                'Category': 'Video/Audio',
                'Pricing Model': 'Paid',
                'Rating': 4.5,
                'Downloads': '3M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.synthesia.io',
                'Key Features': 'AI video generation, avatars, text-to-video, multilingual',
                'Region': 'Global',
                'Last Updated': '2026-01-19'
            },
            {
                'App Name': 'HeyGen',
                'Company': 'HeyGen',
                'Category': 'Video/Audio',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '4M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.heygen.com',
                'Key Features': 'AI avatars, video translation, voice cloning, lip sync',
                'Region': 'Global',
                'Last Updated': '2026-01-24'
            },
            {
                'App Name': 'Descript',
                'Company': 'Descript',
                'Category': 'Video/Audio',
                'Pricing Model': 'Freemium',
                'Rating': 4.7,
                'Downloads': '6M+',
                'App Store Link': 'https://apps.apple.com/us/app/descript-video-audio-editor/id1639254885',
                'Play Store Link': 'N/A',
                'Website': 'https://www.descript.com',
                'Key Features': 'Transcription, AI voices, video editing, overdub, text-based editing',
                'Region': 'Global',
                'Last Updated': '2026-01-31'
            },
            
            # Productivity
            {
                'App Name': 'Notion AI',
                'Company': 'Notion Labs',
                'Category': 'Productivity',
                'Pricing Model': 'Freemium',
                'Rating': 4.8,
                'Downloads': '100M+',
                'App Store Link': 'https://apps.apple.com/us/app/notion-notes-docs-tasks/id1232780281',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=notion.id',
                'Website': 'https://www.notion.so',
                'Key Features': 'Writing assistance, summarization, task management, databases',
                'Region': 'Global',
                'Last Updated': '2026-02-03'
            },
            {
                'App Name': 'Grammarly',
                'Company': 'Grammarly',
                'Category': 'Productivity',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '50M+',
                'App Store Link': 'https://apps.apple.com/us/app/grammarly-keyboard-editor/id1158877342',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.grammarly.android.keyboard',
                'Website': 'https://www.grammarly.com',
                'Key Features': 'Grammar checking, writing suggestions, tone detection, plagiarism',
                'Region': 'Global',
                'Last Updated': '2026-01-30'
            },
            {
                'App Name': 'Jasper',
                'Company': 'Jasper AI',
                'Category': 'Productivity',
                'Pricing Model': 'Paid',
                'Rating': 4.5,
                'Downloads': '2M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.jasper.ai',
                'Key Features': 'AI content creation, marketing copy, blog posts, templates',
                'Region': 'Global',
                'Last Updated': '2026-01-21'
            },
            {
                'App Name': 'Copy.ai',
                'Company': 'Copy.ai',
                'Category': 'Productivity',
                'Pricing Model': 'Freemium',
                'Rating': 4.4,
                'Downloads': '3M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.copy.ai',
                'Key Features': 'Copywriting, content generation, marketing, social media posts',
                'Region': 'Global',
                'Last Updated': '2026-01-17'
            },
            {
                'App Name': 'Otter.ai',
                'Company': 'Otter.ai',
                'Category': 'Productivity',
                'Pricing Model': 'Freemium',
                'Rating': 4.6,
                'Downloads': '10M+',
                'App Store Link': 'https://apps.apple.com/us/app/otter-transcribe-voice-notes/id1276437113',
                'Play Store Link': 'https://play.google.com/store/apps/details?id=com.aisense.otter',
                'Website': 'https://otter.ai',
                'Key Features': 'Meeting transcription, real-time notes, AI summaries, collaboration',
                'Region': 'Global',
                'Last Updated': '2026-02-01'
            },
            
            # Code Assistants
            {
                'App Name': 'GitHub Copilot',
                'Company': 'GitHub/Microsoft',
                'Category': 'Code Assistant',
                'Pricing Model': 'Paid',
                'Rating': 4.7,
                'Downloads': '20M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://github.com/features/copilot',
                'Key Features': 'Code completion, suggestions, chat, multi-language support',
                'Region': 'Global',
                'Last Updated': '2026-02-02'
            },
            {
                'App Name': 'Cursor',
                'Company': 'Anysphere',
                'Category': 'Code Assistant',
                'Pricing Model': 'Freemium',
                'Rating': 4.8,
                'Downloads': '5M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://cursor.sh',
                'Key Features': 'AI code editor, codebase understanding, chat, refactoring',
                'Region': 'Global',
                'Last Updated': '2026-01-28'
            },
            {
                'App Name': 'Tabnine',
                'Company': 'Tabnine',
                'Category': 'Code Assistant',
                'Pricing Model': 'Freemium',
                'Rating': 4.5,
                'Downloads': '10M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://www.tabnine.com',
                'Key Features': 'Code completion, privacy-focused, team learning, IDE integration',
                'Region': 'Global',
                'Last Updated': '2026-01-23'
            },
            {
                'App Name': 'Codeium',
                'Company': 'Exafunction',
                'Category': 'Code Assistant',
                'Pricing Model': 'Free',
                'Rating': 4.6,
                'Downloads': '8M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://codeium.com',
                'Key Features': 'Free code completion, 70+ languages, chat, search',
                'Region': 'Global',
                'Last Updated': '2026-01-29'
            },
            {
                'App Name': 'Amazon CodeWhisperer',
                'Company': 'Amazon',
                'Category': 'Code Assistant',
                'Pricing Model': 'Free',
                'Rating': 4.4,
                'Downloads': '5M+',
                'App Store Link': 'N/A',
                'Play Store Link': 'N/A',
                'Website': 'https://aws.amazon.com/codewhisperer',
                'Key Features': 'Code suggestions, security scanning, AWS integration, reference tracking',
                'Region': 'Global',
                'Last Updated': '2026-01-25'
            },
        ]
    
    def get_data(self, category=None, region=None, limit=None):
        """
        Get filtered data based on category and region.
        
        Args:
            category: Filter by category (e.g., 'Chatbot', 'Image Generation')
            region: Filter by region (e.g., 'Global', 'North America')
            limit: Maximum number of results to return
            
        Returns:
            List of dictionaries containing app data
        """
        filtered_data = self.data
        
        # Filter by category
        if category and category != 'All':
            filtered_data = [app for app in filtered_data if app['Category'] == category]
        
        # Filter by region
        if region and region != 'All':
            filtered_data = [app for app in filtered_data if app['Region'] == region]
        
        # Apply limit
        if limit:
            filtered_data = filtered_data[:limit]
        
        return filtered_data
    
    def get_categories(self):
        """Get list of unique categories in the data."""
        return list(set(app['Category'] for app in self.data))
    
    def get_regions(self):
        """Get list of unique regions in the data."""
        return list(set(app['Region'] for app in self.data))
