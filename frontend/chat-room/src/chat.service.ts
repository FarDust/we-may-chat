import * as io from 'socket.io-client';
import { Observable } from 'rxjs';

export class ChatService {
    private url = 'http://localhost:8000';
    private socket;    

    constructor() {
        this.socket = io(this.url);
    }

    public sendMessage(message) {
      this.socket.emit('chat-message', message);
    }
    
    public getMessages = () => {
        return Observable.create((observer) => {
            this.socket.on('chat-message', (message) => {
                observer.next(message);
            });
        });
    }
}