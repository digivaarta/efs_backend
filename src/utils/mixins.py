from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from utils.pagination import CustomPagination


class AbstractUpdateAPI(UpdateAPIView):

    def get_object(self):
        serializer = self.serializer_class()
        return serializer.get_object(self.request.user)

    def get(self, request):
        profile = self.serializer_class(self.get_object())
        return Response(profile.data)

    def update(self, request, *args, **kwargs):
        print(request)
        instance = self.get_object()
        context = {"request": request}
        serializer = self.serializer_class(
            instance, data=request.data, context=context)
        serializer.is_valid()
        print(serializer.errors)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AbstractPKUpdateAPI(UpdateAPIView):

    def get_object(self):
        pk = self.kwargs["pk"]
        serializer = self.serializer_class()
        return serializer.get_object(pk)

    def get(self,request,pk):
        obj = self.serializer_class(self.get_object())
        return Response(obj.data)

    def update(self,request,*args,**kwargs):
        instance = self.get_object()
        context = {"request":request,"obj_id":self.kwargs["pk"]}
        serializer = self.serializer_class(
            instance,data=request.data,context=context)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AbstractCreateAPI(CreateAPIView):

    def create(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.data, context=context)
        print(request.user)
        serializer.is_valid()
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AbstracLoginAPI(CreateAPIView):

    def create(self,request):
        context = {"request":request}
        serializer = self.serializer_class(data=request.data,context=context)
        if serializer.is_valid():
            result = serializer.login(request.data)
            if result is not None:
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response({"error":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AbstractListAPI(ListAPIView):

    pagination_class = CustomPagination


class AbstractAListAPI(ListAPIView):
    pass


class AbstractDetailAPI(RetrieveAPIView):

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(pk)
        serializer_class = self.get_serializer_class()
        if queryset is not None:
            serializer = serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"submit": False}, status=status.HTTP_400_BAD_REQUEST)


class AbstractRetrieveAPI(RetrieveAPIView):

    def retrieve(self, request, pk=None):
        context = {"request":request}
        queryset = self.get_queryset(pk)
        if queryset is not None:
            serializer = self.serializer_class(queryset,context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"submit": False}, status=status.HTTP_400_BAD_REQUEST)

class AbstractUserRetrieveAPI(RetrieveAPIView):

    def retrieve(self,request,pk=None):
        context = {"request":request}
        queryset= self.get_queryset()
        if queryset is not None:
            serializer = self.serializer_class(queryset,context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"submit": False}, status=status.HTTP_400_BAD_REQUEST)

class AbstractReverseRetrieveAPI(RetrieveAPIView):

    def retrieve(self, request, pk=None):
        context = {"request":request}
        queryset = self.get_queryset(pk)
        if queryset is not None:
            serializer = self.serializer_class(queryset,context=context)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response({"submit": False}, status=status.HTTP_200_OK)


class AbstractMultipleRetrieveAPI(RetrieveAPIView):

    def retrieve(self,request,sig=None,verify=None):
        context = {"request":request}
        queryset = self.get_queryset(sig,verify)
        if queryset is not None:
            serializer = self.serializer_class(queryset,context=context)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"submit":False},status=status.HTTP_400_BAD_REQUEST)
