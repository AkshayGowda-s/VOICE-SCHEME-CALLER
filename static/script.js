async function fetchScheme() {
  const category = document.getElementById('category').value;
  const keyword = document.getElementById('search').value.trim();
  const language = document.getElementById('language').value;
  const resText = document.getElementById('responseText');
  const audio = document.getElementById('audioPlayer');

  resText.textContent = '⏳ Fetching scheme info...';
  audio.style.display = 'none';
  audio.src = '';

  const useSearch = keyword !== "";

  if (!category && !useSearch) {
    resText.textContent = "❗ Please select a category or enter a search keyword.";
    return;
  }

  const payload = {
    category: useSearch ? 'search' : category,
    language: language,
    keyword: useSearch ? keyword : null
  };

  try {
    const response = await fetch('/get_scheme_audio', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (response.ok) {
      resText.textContent = data.message;
      audio.src = data.audio_path;
      audio.style.display = 'block';

      // 🟢 Auto play the audio when it's ready
      audio.play().catch(err => {
        console.warn("Autoplay blocked. User interaction needed.");
      });
    } else {
      resText.textContent = data.error || "❌ Error fetching scheme.";
    }
  } catch (err) {
    console.error(err);
    resText.textContent = "❌ Something went wrong. Please check the backend.";
  }
}
