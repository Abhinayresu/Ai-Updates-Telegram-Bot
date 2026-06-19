# 🤖 Jimmy: The Gen-Z AI News Anchor

Jimmy is an autonomous Telegram bot that aggregates, curates, and broadcasts the most mind-blowing AI updates directly to your Telegram channel. Tailored for Gen-Z CSE students and young tech entrepreneurs, Jimmy speaks their language (a vibrant mix of Telugu and English) and filters out the noise so your audience only gets the "real deal."

## 🚀 Vision & Strategy

The AI news space is crowded and overwhelming. Jimmy solves this by:
- **Curating the Best:** Aggregating from elite sources (MIT News, Analytics Vidhya, Wired, Emerj, and Google News).
- **Filtering the Noise:** Utilizing **Google Gemini 2.5 Flash** to ruthlessly discard mundane updates and select only the top 2-3 most impactful stories.
- **Audience Resonance:** Writing in an energetic, relatable "Vibecoding" style (Telugu + English) that appeals directly to the Gen-Z demographic.
- **Growth Hacking:** Dynamically generating a unique Call-To-Action (CTA) for the YouTube channel every single day, keeping the audience engaged and driving cross-platform growth.

## 🛠️ Technical Architecture

Jimmy is built for simplicity, reliability, and speed:
- **Core Engine:** Python 3.x
- **AI Brain:** Google Gemini API (`gemini-2.5-flash`) for intelligent curation and natural language generation.
- **Content Ingestion:** `feedparser` to parse RSS feeds from top AI news outlets.
- **Distribution:** Telegram Bot API via `requests` for instant broadcasting.
- **Concurrency Control:** Simple file-based locking (`jimmy.lock`) to prevent duplicate executions.

## 📦 File Structure

- `jimmy_brain.py`: The core operational script. Handles RSS parsing, AI curation, and Telegram broadcasting.
- `jimmy_test.py`: Testing and development playground.

## ⚙️ Setup & Deployment

1. **Clone the Repository**
2. **Install Dependencies:**
   ```bash
   pip install feedparser requests google-generativeai
   ```
3. **Configure Secrets:**
   Update `jimmy_brain.py` with your credentials (or ideally, transition these to environment variables):
   - `GEMINI_API_KEY`: Your Google AI Studio API key.
   - `TELEGRAM_BOT_TOKEN`: Your Telegram Bot token from BotFather.
   - `TELEGRAM_CHANNEL`: The target Telegram channel (e.g., `@aiupdatestelugu`).
4. **Run Jimmy:**
   ```bash
   python jimmy_brain.py
   ```
   *Pro Tip: Schedule this script via Cron (Linux/macOS) or Task Scheduler (Windows) to run daily for an automated news broadcasting system.*

## 🌟 Future Roadmap

- [ ] **Security Enhancement:** Move hardcoded API keys to a `.env` file for safer version control.
- [ ] **Dynamic Feed Management:** Move RSS URLs to an external configuration file or database.
- [ ] **Multi-Language Support:** Expand beyond Telugu/English to target other regional demographics.
- [ ] **Interactive Bot Features:** Allow users to reply to Jimmy for deep dives into specific news stories.
- [ ] **Analytics Dashboard:** Track link clicks and engagement metrics directly within Telegram.

---
*Built with ❤️ for the AI Updates Telugu community.*
