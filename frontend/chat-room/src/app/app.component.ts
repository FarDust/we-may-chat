import { Component, Input } from '@angular/core';
import { ChatService } from '../chat.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'chat-room';
  message: string;
  messages: object[] = [];
  nickname: string = '';
  page = 0;
  pageSize = 5;
  @Input() retrieve_url: string = '/getData/';
  
  constructor(private chatService: ChatService) {
  }

  parseNickname(nickname) { 
    if (nickname === '') {
      return 'Anonymous';
    };
    return nickname;
  }

  sendMessage() {
    let message = {
      content: this.message,
      nickname: this.nickname,
    }
    this.chatService.sendMessage(JSON.stringify(message));
    console.log(this.message);
    this.message = '';
  }

  async ngOnInit() {
    let request = new Request(this.retrieve_url);
    let response = await fetch(request).then((response) => {
      return response.json();
    }).then(data => data);
    this.messages = response;
    this.chatService
      .getMessages()
      .subscribe((message: string) => {
        this.messages.unshift(JSON.parse(message));
      });
  }
}
