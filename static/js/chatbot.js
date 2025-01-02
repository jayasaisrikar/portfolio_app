document.addEventListener('DOMContentLoaded', function() {
    const chatbotToggle = document.querySelector('.chatbot-toggle');
    const chatbotBox = document.querySelector('.chatbot-box');
    const closeChat = document.querySelector('.close-chat');
    const chatInput = document.querySelector('.chat-input input');
    const sendButton = document.querySelector('.send-message');
    const chatMessages = document.querySelector('.chat-messages');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    let isProcessing = false;

    chatbotToggle.addEventListener('click', () => {
        chatbotBox.classList.add('active');
    });

    closeChat.addEventListener('click', () => {
        chatbotBox.classList.remove('active');
    });

    async function sendMessage() {
        if (isProcessing) return;
        
        const message = chatInput.value.trim();
        if (message) {
            isProcessing = true;
            addMessage('user', message);
            chatInput.value = '';
            
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message bot typing';
            typingDiv.innerHTML = `
                <i class="fas fa-robot"></i>
                <p>Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></p>
            `;
            chatMessages.appendChild(typingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            try {
                const formData = new FormData();
                formData.append('message', message);

                const response = await fetch('/chatbot-response/', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken
                    },
                    body: formData
                });

                const data = await response.json();
                typingDiv.remove();

                if (data.error) {
                    addMessage('bot', 'Sorry, I encountered an error. Please try again.');
                } else {
                    addMessage('bot', data.response);
                }
            } catch (error) {
                typingDiv.remove();
                addMessage('bot', 'Sorry, I encountered an error. Please try again.');
            } finally {
                isProcessing = false;
            }
        }
    }

    function addMessage(type, text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.innerHTML = `
            <i class="fas fa-${type === 'bot' ? 'robot' : 'user'}"></i>
            <p>${text}</p>
        `;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    sendButton.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !isProcessing) {
            sendMessage();
        }
    });
}); 