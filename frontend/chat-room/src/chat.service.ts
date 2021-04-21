import {io} from 'socket.io-client';
import { Observable } from 'rxjs';
import { Injectable } from "@angular/core";

@Injectable()
export class ChatService {
    private url = '/';
    private socket;    

    constructor() {
        this.socket = io(this.url);
    }

    public sendAudio(audio) {
        this.socket.emit('audio-message', audio);
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