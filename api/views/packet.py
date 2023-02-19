from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import SharedPacketSerializers
from rest_framework.parsers import MultiPartParser, FormParser

@api_view([POST])
@parser_classes([MultiPartParser,FormParser])
def create_packet(request):
    serializer = SharedPacketSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view([GET,PUT,DELETE])
def manage_packet(request,packet_id):
    try:
        packet = SharedPacket.objects.get(packet_id=packet_id)
        if request.method == GET:
            serializer = SharedPacketSerializers(packet)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == PUT:
            serializer = SharedPacketSerializers(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == DELETE:
            packet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except SharedPacket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)