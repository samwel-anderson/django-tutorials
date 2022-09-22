from rest_framework import serializers

from tutorials2_books.models_base import Books


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = (
            'id',
            'book_id',
            'bookname',
            'category',
            'created_at'
        )


#
# class ChatRoomSerializer(serializers.ModelSerializer):
#     subtopic_name = serializers.ReadOnlyField(source='subtopic.subtopic_name')
#     messages = MessagesSerializer(source='lcms_olevel_messages_set', many=True, read_only=True)
#     subtopic_id = serializers.IntegerField(write_only=True)
#     session = serializers.CharField(write_only=True)
#     message = serializers.CharField(write_only=True)
#
#     class Meta:
#         ref_name = "ChatRooms"
#         model = ChatRoom
#         fields = ('id', 'icon', 'subtopic_name', 'messages', 'subtopic_id', 'session', 'message')
