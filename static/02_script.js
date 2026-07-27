// Smooth scroll for anchors
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // --- RepoMind Frontend Logic ---

    const repoInput = document.getElementById('repo-input');
    const actionBtn = document.getElementById('action-btn');
    const terminalContent = document.getElementById('terminal-content');

    let isIndexed = false;
    const API_BASE_URL = 'http://127.0.0.1:5000'; // Default Flask port

    function appendToTerminal(text, type = 'info') {
        const p = document.createElement('p');
        p.className = 'mt-1';

        if (type === 'error') p.className += ' text-red-400';
        else if (type === 'success') p.className += ' text-green-400';
        else if (type === 'question') p.className += ' text-pink-400';
        else if (type === 'answer') p.className += ' text-slate-300 border-l-2 border-blue-500 pl-4 py-2 bg-blue-500/5';
        else p.className += ' text-slate-300'; // default info

        // specific formatting for Q&A
        if (type === 'question') {
            p.innerHTML = `<span class="text-pink-400">Question:</span> "${text}"`;
        } else if (type === 'answer') {
            p.innerHTML = `<span class="text-blue-400 font-bold">Answer:</span> ${text}`;
        } else {
            p.textContent = text;
        }

        terminalContent.appendChild(p);
        // Auto scroll to bottom
        terminalContent.scrollTop = terminalContent.scrollHeight;
    }

    actionBtn.addEventListener('click', async () => {
        const value = repoInput.value.trim();
        if (!value) return;

        actionBtn.disabled = true;
        actionBtn.classList.add('opacity-50', 'cursor-not-allowed');

        if (!isIndexed) {
            // MODE: Indexing
            const repoUrl = value;
            appendToTerminal(`> index ${repoUrl}`, 'info');
            appendToTerminal('Starting indexing process... this may take a while.', 'info');

            try {
                const response = await fetch(`${API_BASE_URL}/api/index-repo`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ repo_url: repoUrl })
                });

                const data = await response.json();

                if (response.ok) {
                    appendToTerminal('✓ Repository indexed successfully.', 'success');
                    repoInput.value = '';
                    repoInput.placeholder = 'Ask a question about the codebase...';
                    actionBtn.textContent = 'Ask';
                    isIndexed = true;
                } else {
                    appendToTerminal(`Error: ${data.error || 'Failed to index'}`, 'error');
                }
            } catch (err) {
                appendToTerminal(`Network Error: ${err.message}. Is the backend running?`, 'error');
            }

        } else {
            // MODE: Chatting
            const question = value;
            appendToTerminal(question, 'question');
            repoInput.value = '';

            try {
                const response = await fetch(`${API_BASE_URL}/api/chat`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: question })
                });

                const data = await response.json();

                if (response.ok) {
                    appendToTerminal(data.answer, 'answer');
                } else {
                    appendToTerminal(`Error: ${data.error || 'Failed to get answer'}`, 'error');
                }
            } catch (err) {
                appendToTerminal(`Network Error: ${err.message}`, 'error');
            }
        }

        actionBtn.disabled = false;
        actionBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    });

    // Allow pressing Enter to submit
    repoInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            actionBtn.click();
        }
    });

    // Clear initial mock content when user first interacts if desired
    // For now we append to it.
});
